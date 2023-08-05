#!/usr/bin/env python3

from netdevice import linux
import simplejson as json
import pexpect
import xmltodict
import ipaddress
import random
from lxml import etree
try:
    # Python 2.
    from StringIO import StringIO
    # Python 3.
except ImportError:
    from io import StringIO
import sys, os, time
import collections
import tempfile

class OvsHost(linux.LinuxDevice):
    '''
    OvsHost is a linux host with OpenvSwitch installed. You can build the
    topology and run test on it.

    Now it integerate the docker and can connect the container automatically.
    '''
    def __init__ (self, server = None, **kwargs):
        '''
        Connect the host and start the OVS.
        '''

        linux.LinuxDevice.__init__(self, server, **kwargs)

        # start the docker if it's not running
        num = self.cmd('ps -ef | grep -w ovs-vswitchd | grep -v grep | wc -l')
        if num and int(num) <= 0:
            self.cmd('ovs-ctl start')
            self.cmd('ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true')
            self.log("Setup OVS complete")

        if (self["log_level"] >= 7):
            #LOG_DEBUG = 7
            self.cmd('ovs-appctl vlog/set ANY:file:dbg')
            #self.cmd('echo > /usr/local/var/log/openvswitch/ovsdb-server.log')
            self.cmd('echo > /usr/local/var/log/openvswitch/ovs-vswitchd.log')

        # start the docker if it's not running
        num = self.cmd('ps -ef | grep -w dockerd | grep -v grep | wc -l')
        if num and int(num) <= 0:
            self.cmd('systemctl start docker')
        self.log("Setup docker complete")

    def __del__(self):
        '''
        Get the trace file.
        Don't stop the OVS or docker.
        '''
        # postconfig
        self.log("%s.%s(%s), finish in %.2f seconds\n" %(self.__class__.__name__,
            sys._getframe().f_code.co_name,
            self.version,
            time.time() - self.start_time))

        if (self["log_level"] >= 7):
            #self.get_file('/usr/local/var/log/openvswitch/ovsdb-server.log',
            #        "%s_ovsdb-server.log" %(self["name"]))
            self.get_file('/usr/local/var/log/openvswitch/ovs-vswitchd.log',
                    "%s_ovs-vswitched.log" %(self["name"]))

        # restore the log level to default
        num = self.cmd('ps -ef | grep -w ovs-vswitchd | grep -v grep | wc -l')
        if num and int(num) > 0:
            self.cmd('ovs-appctl vlog/set ANY:file:info')

    def ovs_connect (self, bridge, *args, **kwargs):
        '''
        Build the subnet: Create a bridge and connect something to it. Now it
        support container and physicial network card. it will support vm and
        physical devices later.

        A bridge looks like this:

            vm1_br_int = {"name": "br-int",
                          "datapath_type": "netdev",
                          "port": [ {"name": "vxlan0",
                                      "type": "vxlan",
                                      "options:remote_ip": "192.168.63.113",
                                      "options:key": "flow" }, ]}

        args are network devices, for exampe a phisicial device, virtual
        machine, or a container, etc. it may looks like this:

            con1 = {"name": "con1",
                    "type": "container",
                    "interface": "eth1",
                    "ip": "10.208.1.11/24"}

        '''
        bridge_name = bridge.pop("name", None) #get bridge name
        ports = bridge.pop("port", []) # get the ports list
        ports = ports if (isinstance(ports, list)) else [ports]

        # Create the bridge
        command = 'ovs-vsctl --may-exist add-br %s' %(bridge_name)
        if bridge:
            # If there is parameters, for example datapath_type, etc.
            command += ' -- set bridge %s' %(bridge_name)
            for k,v in bridge.items():
                command += ' %s=%s' %(k,v)
        self.cmd(command) #execut the command.

        # Add self-port
        for p in ports:
            port_name = p.pop("name", None)
            command = 'ovs-vsctl add-port %s %s' %(bridge_name, port_name)
            if p:
                # If there is parameters, for example type=vxlan, etc.
                command += ' -- set interface %s' %(port_name)
                for k,v in p.items():
                    command += ' %s=%s' %(k,v)
            self.cmd(command) #execut the command.

        # Add remote-device and it's peer self-port
        for d in args:
            peer_type = d.get("type", None)
            if peer_type == "container":
                # Create a container and the self-port
                self.cmd(
                    'docker run --privileged -d --name %s -v %s:%s -it centos'
                    %(d["name"], d.get("host_dir", "/var/shared"),
                    d.get("container_dir", "/var/shared")))

                #Allocate the interface/ipaddress and connect it to ovs bridge
                self.cmd('ovs-docker add-port %s %s %s --ipaddress=%s'
                        %(bridge_name, d["interface"], d["name"], d["ip"]))

            elif peer_type == "phy":
                # Configure the physicial network card and Add it to the bridge
                self.cmd('ovs-vsctl add-port %s %s' %(bridge_name, d["name"]))
                self.cmd('ip address add %s dev %s'
                        %(d["ip"], bridge_name))
                self.cmd('ip link set %s up' %(bridge_name))
                self.cmd('ip addr flush dev %s 2>/dev/null' %(d["name"]))
                self.cmd('ip link set %s up' %(d["name"]))
                self.cmd('iptables -F')
                #vm1.cmd('ovs-appctl ovs/route/add %s br-phy' %(d["ip"]))
                #vm1.cmd('ovs-appctl ovs/route/show')
            elif peer_type == "dpdk":
                # A dpdk network card
                command = 'ovs-vsctl add-port %s %s' %(bridge_name, d["name"])
                command += ' -- set interface %s type=%s' %(d["name"], d["type"])
                if d.get("options", None):
                    command += 'options:%s' %(d["options"])
                self.cmd(command)

                self.cmd('ip address add %s dev %s'
                        %(d["ip"], bridge_name))
                self.cmd('ip link set %s up' %(d["name"]))
                self.cmd('iptables -F')
            else:
                self.log("type %s is not supported now..." %(t))

            # Configure vlan on self-port if the device has vlan configured.
            if d.get("vlan", None):
                self.cmd(
                    'ovs-vsctl set port %s tag=%d'
                    %(ovs_get_port(bridge_name, name = d["name"]), d["vlan"]))

    def ovs_get_topology (self, *args, **kwargs):
        '''
        Destroy the topology:

            * Destroy the OVS and all its bridges.
            * Destroy all the devices connected to it if given in the *args.
        '''
        # delete all the bridges in the OVS
        #topology = {"name": self["name"], "bridges": [] }
        topology = []
        bridges = self.cmd("ovs-vsctl list-br")
        for b in StringIO(bridges).readlines():
            #print("Bridge %s" %(b.strip()))
            topology.append("Bridge %s" %(b.strip()))
            #bridge = {"name": b.strip(), "ports": []}
            ports = self.cmd("ovs-vsctl list-ports %s" %(b.strip()))
            for p in StringIO(ports).readlines():
                external_ids = self.cmd(
                 "ovs-vsctl list interface %s | awk -F: '/external_ids/ {print $2}'"
                  %(p.strip()))
                if (external_ids.strip() != "{}"):
                    topology.append("    Port %s, external_ids: %s"
                            %(p.strip(), external_ids.strip()))

                options = self.cmd(
                 "ovs-vsctl list interface %s | awk -F: '/options/ {print $2}'"
                  %(p.strip()))
                if (options.strip() != "{}"):
                    topology.append("    Port %s, options: %s"
                            %(p.strip(), options.strip()))

                link_speed = self.cmd(
                 "ovs-vsctl list interface %s | awk -F: '/link_speed/ {print $2}'"
                  %(p.strip()))
                if (options.strip() != "[]"):
                    topology.append("    Port %s, link_speed: %s"
                            %(p.strip(), link_speed.strip()))
                #port = {"name": p.strip(), "interface": p.strip()}
                #print("    Port %s %s" %(p.strip(), external_ids.strip()))
                #bridge["ports"].append(port)
            #topology["bridges"].append(bridge)
        #self.log("container: %s\n" %(json.dumps(topology, indent=4)))
        for i in topology:
            print(i)

    def ovs_destroy (self, *args, **kwargs):
        '''
        Destroy the topology:

            * Destroy the OVS and all its bridges.
            * Destroy all the devices connected to it if given in the *args.
        '''
        # delete all the bridges in the OVS
        bridges = self.cmd("ovs-vsctl list-br")
        for i in StringIO(bridges).readlines():
            #ports = self.cmd("ovs-vsctl list-ports %s" %(i.strip()))
            self.cmd("ovs-vsctl del-br %s" %(i.strip()))
        #self.cmd('ovs-vsctl show')
        self.cmd('ovs-ctl stop')

        # delete all the devices(container/vm/physical) that it connect to.
        for d in args:
            if d["type"] == "container":
                self.cmd('docker stop %s' %(d["name"]))
                self.cmd('docker rm %s' %(d["name"]))
            elif d["type"] == "vm":
                self.log("type %s is not supported now..." %(d["type"]))

    def ovs_get_port (self, bridge, **kwargs):
        '''
        Get a self-port which connect to the kwargs["name"]
        '''
        ports = self.cmd("ovs-vsctl list-ports %s" %(bridge))
        for p in StringIO(ports).readlines():
            #external_ids = self.cmd(
            # "ovs-vsctl list interface %s | awk -F: '/external_ids/ {print $2}'"
            #  %(p.strip()))
            external_ids = self.cmd("ovs-vsctl list interface %s | grep external_ids"
                    %(p.strip()))
            r = re.findall('{container_id=(.*),', external_ids)
            if (r and r[0] == kwargs.get("name", None)):
                return p.strip()
        return None

    def ovs_add_flows (self, bridge, *args, **kwargs):
        '''
        Add some flows to ofproto
        '''

        for table in args:
            table = filter(lambda x: (x.strip()) and (x.strip()[0] != '#'),
                    StringIO(table.strip()).readlines())
            for l in table:
                # remove the line starting with '#'
                self.cmd('ovs-ofctl add-flow %s "%s"'
                        %(bridge["name"], l.strip()))
        return None


if __name__ == '__main__':
    '''
    #topology：
        (vr1)vrl1 -- vsl1(dvs1)vsl1 -- vrl1(vr1)
    '''

    vm1 = OvsHost("ssh://root:sangfor@172.93.63.111", name = "vm1",
            log_color = "red", log_level = options.log_level)
    vm1_br_int = {"name": "br-int", "datapath_type": "netdev",
            "port": [ {"name": "vxlan0", "type": "vxlan",
                "options:remote_ip": "192.168.63.113", "options:key": "flow" }]}
    vm1_br_phy = {"name": "br-phy", "datapath_type": "netdev",
            "other_config:hwaddr": "fe:fc:fe:b1:1d:0b",
            }
    vm1_eth1 = {"name": "eth1", "type": "phy", "ip": "192.168.63.111/16"}
    con = []
    for i in range(4):
        con.append({"name": "con%d"%(i), "type": "container", "interface": "eth1",
            "ip": "10.208.1.%d/24" %(10+i)})
    vm1.log("container: %s\n" %(json.dumps(con, indent=4)))
    vm1.cmd('ovs-vsctl show')

    vm1.ovs_connect(vm1_br_int, con[0], con[1])
    vm1.ovs_connect(vm1_br_phy, vm1_eth1)
    vm1.cmd('ovs-vsctl show')
