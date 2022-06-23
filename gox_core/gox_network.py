# Copyright 2022 <Alex DANDURAN--LEMBEZAT, Fetia BANNOUR, Stefania DUMBRAVA>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Handles network events and functions for GOX

Depends on "openflow.discovery" and "misc.host_tracker" to discover
the network topology
"""

from pox.core import core
from pox.lib.revent import *
from pox.lib.util import dpid_to_str


import gox_db
import time

log = core.getLogger()

# network -> POX -> neo4j -> POX -> network

class NetworkEventHandler():

    def __init__(self, db_instance):
        core.listen_to_dependencies(self)   # Creates listeners for events coming from a dependent component
        self.db_instance = db_instance
        log.info("NetworkEventHandler launched")

    def _handle_openflow_discovery_LinkEvent(self, event):
        """
        Handles the event "LinkEvent" from the component "discovery"
        The component "discovery" registered itself as "openflow_discovery"

        Used to discover links on the network and track their state.
        """
        # log.info("Handling openflow discovery LinkEvent event")

        dpid1=dpid_to_str(event.link.dpid1)
        dpid2=dpid_to_str(event.link.dpid2)
        port1=event.port_for_dpid(event.link.dpid1)
        port2=event.port_for_dpid(event.link.dpid2)
        
        # Switchs/Hosts exist ?
        if(not self.db_instance.entityExists(dpid1) or not self.db_instance.entityExists(dpid2)):
            log.warn("Impossible to add link. Nodes {0} or {1} do not exist !".format(dpid1, dpid2))
            return
        
        # Has the link been added or removed ?
        if(event.added):
            if self.db_instance.linkExists(dpid1, port1, dpid2, port2):
                log.warn("Link {0}.{1} -> {2}.{3} already in the database".format(dpid1, port1, dpid2, port2))
                return  
            else:
                self.db_instance.addLink(dpid1, port1, dpid2, port2)
                log.info("Link {0}.{1} <-> {2}.{3} added".format(dpid1, port1, dpid2, port2))
        elif(event.removed):
            if not self.db_instance.linkExists(dpid1, port1, dpid2, port2):
                log.warn("Link {0}.{1} -> {2}.{3} not in database".format(dpid1, port1, dpid2, port2))
                return  
            else:
                self.db_instance.delLink(dpid1, port1, dpid2, port2)
                log.info("Link {0}.{1} <-/-> {2}.{3} removed".format(dpid1, port1, dpid2, port2))

    # _handle_<ComponentName>_<EventName>
    def _handle_host_tracker_HostEvent(self, event):
        """
        Handles the event "HostEvent" from the component "host_tracker"
        Used to discover hosts on the network and track their state

        The component Discovery does not handle the detection of links between
        hosts and switches. We have to create them here
        """
        # log.info("Handling host_tracker HostEvent event")

        mac = str(event.entry.macaddr)
        ip = " " # event.entry.ipAddrs.keys()[0]
        switchPort = event.entry.port
        switchDpid = dpid_to_str(event.entry.dpid)

        if (event.join):
            # Was the host disconnected ?
            if(self.db_instance.hostExists(mac)):
                log.warn("HostEvent : (Join) Impossible to handle event, Host {} already exists.".format(mac))
                return
            # Does the switch the host is connected to exist ?
            if(not self.db_instance.switchExists(switchDpid)):
                log.warn("HostEvent : (Join) Impossible to handle event, Switch {} does not exist.".format(switchDpid))
                return
            
            # print(event.entry.ipAddrs)
            self.db_instance.addHost(mac, ip)
            self.db_instance.addLink(mac, "0", switchDpid, switchPort)            
            
        elif (event.leave):
            # Was the host connected ?
            if(not self.db_instance.hostExists(mac)):
                log.warn("HostEvent : (Leave) Impossible to handle event, Host {} does not exist.".format(mac))
                return
            
            self.db_instance.delHost(mac) # All links are also deleted

        elif (event.move):
            # If the host is disconnected
            if(not self.db_instance.hostExists(mac)):
                log.warn("HostEvent : (Move) Impossible to handle event, Host {} does not exist.".format(mac))
                return
            else:
                self.db_instance.delHost(mac)
                if(not self.db_instance.switchExists(switchDpid)):
                    log.warn("HostEvent : (Move) Impossible to handle event, Switch {} does not exist.".format(switchDpid))
                    return
                self.db_instance.addHost(mac, ip)
                self.db_instance.addLink(mac, "0", switchDpid, switchPort)   
        

    def _handle_openflow_ConnectionUp(self, event):
        """
        Handles the event "ConnectionUp" from "of_01.py" and its Connection class
        Happens when a new TCP session is made between a switch and the controller
        """
        # log.info("Handling openflow ConnectionUp event")

        dpid = dpid_to_str(event.dpid)

        if(self.db_instance.entityExists(dpid)):
            log.warn("ConnectionUp : Impossible to handle event, Switch {} already exists".format(dpid))
            return
        
        self.db_instance.addSwitch(dpid)

    def _handle_openflow_ConnectionDown(self, event):
        """
        Handles the event "ConnectionUp" from "of_01.py" and its Connection class
        Happens when a new TCP session is dropped between a switch and the controller
        """
        # log.info("Handling openflow ConnectionDown event")

        dpid = dpid_to_str(event.dpid)

        if(not self.db_instance.entityExists(dpid)):
            log.warn("ConnectionDown : Impossible to handle event, Switch {} does not exist".format(dpid))
            return
        
        self.db_instance.delSwitch(dpid)



def launch():
    print("gox.network is not meant to be executed alone. You should execute gox which handles the execution of the required scripts.")
