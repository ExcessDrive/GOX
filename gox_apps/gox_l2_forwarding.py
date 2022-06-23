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

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.revent import *
from pox.lib.addresses import EthAddr
import time


log = core.getLogger()

# Flow timeouts
FLOW_IDLE_TIMEOUT = 10
FLOW_HARD_TIMEOUT = 30

class GoxForwarding(object):
    """
    Forward packets according to the shortest path defined in neo4j's 
    Graph Data Science library. It uses Dijkstra's algorithm.

    Inspired from forwarding.l2_learning and Gavel's routing script
    """

    def __init__(self):
        core.openflow.addListeners(self)

        self.db_session = core.DatabaseInstance.session
        log.info("GoxForwarding ready")
        
    
    def craftOpenflowMessage(self, src_mac, dst_mac, out_port, data = None):
        """
        Method for crafting an openflow message to forward packets to an output port on a given switch (identified by its dpid)
        """
        msg = of.ofp_flow_mod()
        # msg.idle_timeout = FLOW_IDLE_TIMEOUT
        # msg.hard_timeout = FLOW_HARD_TIMEOUT
        msg.match = of.ofp_match()
        # msg.match.in_port = in_port
        msg.match.dl_src = src_mac
        msg.match.dl_dst = dst_mac
        if data is not None:
            msg.data = data
        msg.actions.append(of.ofp_action_output(port=out_port))
        return msg
        
    def pathExists(self, mac1, mac2):
        """
        Returns a boolean telling if a path between mac1 and mac2 already exists in the database
        """
        query = '''
                MATCH (h1:Host {{mac:"{mac1}"}})-[r:Path_to]-(h2:Host {{mac:"{mac2}"}})
                RETURN r
                '''.format(mac1=mac1, mac2=mac2)
        result = self.db_session.run(query)
        return result.peek() != None

    def sendOFMessages(self, mac1, mac2, switches, in_ports, out_ports, r_in_ports, r_out_ports, event):
        """
        docstring
        """
        packet_out_port = None
        for i in range(len(switches)):
            connection = core.openflow.getConnection(str_to_dpid(switches[i]))
            connection.send(self.craftOpenflowMessage(EthAddr(mac1), EthAddr(mac2), int(out_ports[i])))
            j = len(switches)-i-1
            connection.send(self.craftOpenflowMessage(EthAddr(mac2), EthAddr(mac1), int(r_out_ports[j])))

            if connection == event.connection:
                packet_out_port = int(out_ports[i])

        if packet_out_port is not None:
            packet = event.parsed
            event.connection.send(self.craftOpenflowMessage(packet.src, packet.dst, packet_out_port, event.ofp))


    def installExistingPath(self, mac1, mac2, event):
        """
        Function using the neo4j database for retrieving the previously calculated
        path between 2 hosts and sending it back to the corresponding switches
        """
        query = '''
                MATCH (h1:Host {{mac:"{mac1}"}})-[r1:Path_to]->(h2:Host {{mac:"{mac2}"}})
                MATCH (h1:Host {{mac:"{mac1}"}})<-[r2:Path_to]-(h2:Host {{mac:"{mac2}"}})
                WITH r1.switches AS switches,
                     r1.in_ports AS in_ports, r2.in_ports AS r_in_ports,
                     r1.out_ports AS out_ports, r2.out_ports AS r_out_ports
                    
                RETURN *
                '''.format(mac1=mac1, mac2=mac2)
        result = self.db_session.run(query)

        for record in result:
            self.sendOFMessages(mac1, mac2, record["switches"], record["in_ports"], record["out_ports"], record["r_in_ports"], record["r_out_ports"], event)

    def installNewPath(self, mac1, mac2, event):
        """
        Function using the neo4j database for getting the shortest path between
        2 hosts given their mac adress
        """

        query = '''
                MATCH (h1:Host {{mac:"{mac1}"}})
                MATCH (h2:Host {{mac:"{mac2}"}})
                MATCH p = shortestPath( (h1)-[:Connected_to*]->(h2) )

                WITH h1, h2, p, 
                [n in nodes(p)[1..-1]| n.dpid] AS switches, 
                [r in relationships(p)[1..]| r.orig_port] AS out_ports, 
                [r in relationships(p)[..-1]| r.dst_port] AS in_ports

                WITH *,
                reverse(switches) AS r_switches,
                reverse(in_ports) AS r_in_ports,
                reverse(out_ports) AS r_out_ports

                MERGE (h1)-[p1:Path_to]->(h2)
                ON CREATE SET p1.switches=switches,
                              p1.out_ports=out_ports,
                              p1.in_ports=in_ports

                MERGE (h1)<-[p2:Path_to]-(h2)
                ON CREATE SET p2.switches = r_switches,
                              p2.out_ports = r_in_ports,
                              p2.in_ports = r_out_ports
                
                RETURN switches, in_ports, out_ports, r_out_ports, r_in_ports
                '''.format(mac1=mac1, mac2=mac2)
        result = self.db_session.run(query)
        
        for record in result:
            self.sendOFMessages(mac1, mac2, record["switches"], record["in_ports"], record["out_ports"], record["r_out_ports"], record["r_in_ports"], event)

# <Record switches=['00-00-00-00-00-03', '00-00-00-00-00-01', '00-00-00-00-00-02'] in_ports=['1', '2', '6'] out_ports=['6', '1', '2'] r_switches=['00-00-00-00-00-02', '00-00-00-00-00-01', '00-00-00-00-00-03'] r_out_ports=['2', '1', '6'] r_in_ports=['6', '2', '1']>


    def _handle_PacketIn(self, event):
        """
        Handle packets coming from the switch so as to route them with the shortestpath
        """
        self.connection = event.connection
        sw_dpid = str(self.connection.eth_addr)
        _flood_delay = 0
        
        def flood (message = None):
            """ Floods the packet """
            msg = of.ofp_packet_out()
            msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
            msg.data = event.ofp
            event.connection.send(msg)
            
        def drop (duration = None):
            """
            Drops this packet and optionally installs a flow to continue
            dropping similar ones for a while
            """
            if duration is not None:
                if not isinstance(duration, tuple):
                    duration = (duration,duration)
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = duration[0]
                msg.hard_timeout = duration[1]
                msg.buffer_id = event.ofp.buffer_id
                self.connection.send(msg)
            elif event.ofp.buffer_id is not None:
                msg = of.ofp_packet_out()
                msg.buffer_id = event.ofp.buffer_id
                msg.in_port = event.port
                self.connection.send(msg)

        packet = event.parsed

        if packet.effective_ethertype == packet.LLDP_TYPE:
            drop()
            return

        mac1=str(packet.src)
        mac2=str(packet.dst)
        
        if packet.dst.is_multicast :
            flood() 
        elif core.DatabaseInstance.hostExists(mac1) and core.DatabaseInstance.hostExists(mac2) :
            if self.pathExists(mac1, mac2):
                self.installExistingPath(mac1, mac2, event)
            else:
                self.installNewPath(mac1, mac2, event)
            
        else:
            flood() # If we cannot find the destination, we just flood the packet
        
        


def launch():
    # subscribe to PacketIn event
    if not core.hasComponent("Gox"):
        log.error("Impossible to launch gox_l2_forwarding without launching Gox before")
        return

    core.registerNew(GoxForwarding)





