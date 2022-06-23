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
Handles connections and requests to the neo4j database

The `DatabaseInstance` class contains all information related to the database and how to connect to it.
It also has methods to add or remove some basic components of the basic topology that we provide (hosts, switches, links).

The language used to query neo4j graph databases is Cypher.
"""

from neo4j import GraphDatabase
from pox.core import core

log = core.getLogger()

class DatabaseInstance(object):

    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password
        self.driver = None
        self.session = None

        self.connect()
        self.reset()

        log.info("DatabaseInstance launched")
    
    def connect(self):
        """
        Establishes the connection with the neo4j database thanks to the scheme,
        the ip (usually localhost) and the port on which the database is listening
        """
        self.driver = GraphDatabase.driver(self.uri, auth=(self.username, self.password))
        self.session = self.driver.session()

    def reset(self):
        """
        docstring
        """
        query = '''MATCH (n) DETACH DELETE n'''
        self.session.run(query)

    def addHost(self, mac, ip, name=""):
        query = '''CREATE (:Host {{name: "{host_name}", ip: "{host_ip}", mac: "{host_mac}"}})'''.format(host_name=name, host_ip=ip, host_mac=mac)
        self.session.run(query)

    def delHost(self, mac):
        query = '''
                MATCH (h:Host {{mac: "{host_mac}"}})
                DETACH DELETE h
                '''.format(host_mac=mac)
        self.session.run(query)

    def getHostInfo(self, mac):
        """
        docstring
        """
        query = '''
                MATCH (h:Host {{mac: "{host_mac}"}})
                return h.mac, h.ip, h.name
                '''.format(host_mac=mac)
        result = self.session.run(query)
        res = result.peek()
        return {'mac': res['h.mac'],
                'ip': res['h.ip'],
                'name': res['h.name']} 

    def addSwitch(self, dpid, name=""):
        """
        Adds a switch to the database
        """
        query = '''CREATE (:Switch {{name: "{switch_name}", dpid:"{switch_dpid}"}})'''.format(switch_name=name, switch_dpid=dpid)
        self.session.run(query)

    def delSwitch(self, dpid):
        """
        Removes a switchs and its links from the database
        TODO: if a switch falls, we should remove all the hosts which connect through the switch since they cannot be reached
        """
        query = '''
                MATCH (s:Switch {{dpid:"{switch_dpid}"}})
                DETACH DELETE s
                '''.format(switch_dpid=dpid)
        self.session.run(query)

    def getSwitchInfo(self, dpid):
        """
        docstring
        """
        query = '''
                MATCH (s:Switch {{dpid: "{switch_dpid}"}})
                return s.dpid, s.name
                '''.format(switch_dpid=dpid)
        result = self.session.run(query)
        res = result.peek()
        return {'dpid': res['s.dpid'],
                'name': res['s.name']} 

    def addLink(self, origin_id, origin_port, destination_id, destination_port):
        query = '''
                MATCH (node1) WHERE node1.mac="{orig_id}" OR node1.dpid="{orig_id}"
                MATCH (node2) WHERE node2.mac="{dst_id}" OR node2.dpid="{dst_id}"
                MERGE (node1)-[link1:Connected_to]->(node2)
                ON CREATE SET link1.orig_port="{orig_port}", link1.dst_port="{dst_port}"
                MERGE (node2)-[link2:Connected_to]->(node1)
                ON CREATE SET link2.orig_port="{dst_port}", link2.dst_port="{orig_port}"
                '''.format(orig_id=origin_id, dst_id=destination_id, orig_port=origin_port, dst_port=destination_port)
        self.session.run(query)

    def delLink(self, origin_id, origin_port, destination_id, destination_port):
        """
        Removes a link from the database
        TODO: remove host if it is alone after the link was removed
        """
        query = '''
                MATCH (node1)-[link:Connected_to]-(node2)
                WHERE (node1.mac="{orig_id}" OR node1.dpid="{orig_id}") 
                AND (node2.mac="{dst_id}" OR node2.dpid="{dst_id}")
                AND (link.orig_port="{orig_port}" AND link.dst_port="{dst_port}" OR link.orig_port="{dst_port}" AND link.dst_port="{orig_port}")
                DELETE link
                '''.format(orig_id=origin_id, dst_id=destination_id, orig_port=origin_port, dst_port=destination_port)
        self.session.run(query)

    def linkExists(self, origin_id, origin_port, destination_id, destination_port):
        """
        """
        query = '''
                MATCH (node1)-[link:Connected_to]-(node2)
                WHERE (node1.mac="{orig_id}" OR node1.dpid="{orig_id}")
                AND (node2.mac="{dst_id}" OR node2.dpid="{dst_id}")
                AND (link.orig_port="{orig_port}" AND link.dst_port="{dst_port}" OR link.orig_port="{dst_port}" AND link.dst_port="{orig_port}")
                RETURN link
                '''.format(orig_id=origin_id, dst_id=destination_id, orig_port=origin_port, dst_port=destination_port)
        result = self.session.run(query)

        return result.peek() != None

    def entityExists(self, id):
        """
        Check wether or not an entity (switch or host) exists in the database
        """
        query = '''
                MATCH (node)
                WHERE node.dpid = "{node_id}" OR node.mac = "{node_id}"
                RETURN node
                '''.format(node_id=id)
        result = self.session.run(query)
        return result.peek() != None

    def hostExists(self, mac):
        return self.entityExists(mac)

    def switchExists(self, dpid):
        return self.entityExists(dpid)

    def testMethod(self):
        query = '''
                MATCH (n)
                WHERE n.mac = "h1"
                RETURN n
                '''
        result = self.session.run(query)
        print(result.peek()[0])


def launch():
    print("gox_db is not meant to be executed alone. You should execute gox which handles the execution of the required scripts.")


# For test purposes
if __name__ == "__main__":
    db = DatabaseInstance("bolt://localhost:7687", "neo4j", "password")
    db.reset()
    db.addHost("h1","192.168.1.1")
    db.addHost("h2","192.168.1.2")
    db.addHost("h3","192.168.1.3")
    db.addHost("h4","192.168.1.4")
    db.addHost("h5","192.168.1.5")
    db.addHost("h6","192.168.1.6")
    db.addHost("h7","192.168.1.7")
    db.addHost("h8","192.168.1.8")
    db.addHost("h9","192.168.1.9")
    db.addHost("h10","192.168.1.10")

    db.addSwitch("s1")
    db.addSwitch("s2")
    db.addSwitch("s3")
    db.addSwitch("s4")

    db.addLink("s1","1","h1","0")
    db.addLink("s1","2","h2","0")
    db.addLink("s1","3","h3","0")
    db.addLink("s2","1","h4","0")
    db.addLink("s2","2","h5","0")
    db.addLink("s3","1","h6","0")
    db.addLink("s3","2","h7","0")
    db.addLink("s4","1","h8","0")
    db.addLink("s4","2","h9","0")
    db.addLink("s4","3","h10","0")

    db.addLink("s1","0","s2","0")
    db.addLink("s2","3","s3","0")
    db.addLink("s3","3","s4","0")

    # db.delLink("s2","3","s3","0")




# Neo4j results:
# result.peek() -> 1st result in the form of some kind of dictionary : (result.peek()['h.mac'])
# result.single() -> like .peek() but doesn't consume entry + warning if multiple matchs
# result.data() -> list of dictionnary result.data()[0]["h.mac"]
# result.values() -> list of list containing results : result.values()[0][0]


