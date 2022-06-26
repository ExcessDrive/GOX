# GOX

GOX is a suite of POX components that allow the development of SDN applications that rely on a Neo4j Graph Database-based network topology.

GOX was developed as part of 3-months intership in the ENSIIE engineering school in Evry, France.

## GOX core components

GOX is composed of 3 main core components :

1. **gox**: It is the main component which is tasked with properly starting GOX by launching every secondary components which are essentials 
2. **gox_db**: It is GOX's Neo4j database management component. It handles connections and requests heading to the Neo4j database
3. **gox_network**: It is the script that handles network events and other network functions that GOX requires. It uses *gox_db* script so as to communicate with the database

## GOX's dependencies

The functioning of GOX also depends on the 2 following POX components : 

1. **openflow.discovery**: For registering the connectivity between switches
2. **host_tracker**: For gathering information on the hosts on the network

# Installation

* GOX depends on Python 3 and was developed using Python 3.9.

* GOX depends on POX to function. All the necessary information on how to install and use POX can be found in [POX's documentation](https://noxrepo.github.io/pox-doc/html/)

* To work, GOX needs to be able to connect to a [Neo4j](https://neo4j.com/) database. You can use [Neo4j Server](https://neo4j.com/docs/browser-manual/current/deployment-modes/neo4j-server/) or [Neo4j Desktop](https://neo4j.com/docs/browser-manual/current/deployment-modes/neo4j-desktop/) to create a graph database. 


## Quick Install

If you are on a Debian-based Linux system, you can execute the installation script. 

```bash
git clone https://github.com/ExcessDrive/GOX.git
cd GOX
bash install.sh
```

This script will:

* Add Neo4j's repositories
* Install Neo4j
* Install Neo4j's pip module
* Install Mininet
* Download POX
* Install GOX

You still need to configure your Neo4j server so as to be able to reach it. Especially by decommenting these options in `/etc/neo4j/neo4j.conf`

```
dbms.default_database=neo4j             # Creates default database
dbms.default_listen_address=0.0.0.0     # Accepts to be contacted via any IP address
```

## Manual Install

### Neo4j

First, we should install the Neo4j server that will host the database. To do that, we will follow [Neo4j's official guide](https://debian.neo4j.com/) on installing Neo4j server on a Debian-based machine

```bash
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update
sudo apt install neo4j
```

You also need to install Neo4j's python module with pip:

```bash
pip install neo4j
```

You may as well configure your Neo4j server so as to be able to reach it. Especially by decommenting these options in `/etc/neo4j/neo4j.conf`

```
dbms.default_database=neo4j             # Creates default database
dbms.default_listen_address=0.0.0.0     # Accepts to be contacted via any IP address
```

### Installation of POX and GOX

First, you need to clone the GOX repository:

```bash
git clone https://github.com/ExcessDrive/GOX.git
```

Then, clone the Pox git repository inside the GOX folder:

```bash
cd GOX
git clone https://github.com/noxrepo/pox.git
```

Then, we need to install GOX's core modules and forwarding application in POX:

```bash
cp ./gox_core/* ./pox/ext/
cp ./gox_apps/* ./pox/ext/
```

# Usage

GOX can be started like any other POX component. Only the main core component of GOX called "gox" should be started. Indeed, this component will also launch *gox_db*, *gox_network*, *openflow.discovery* and *host_tracker*.

GOX needs the neo4j database to run:

```bash
sudo neo4j start
```

You need to initialise the Neo4j database by connecting to it for the first time via your web browser `http://<ip>:7474`
The default login is "neo4j" and password is "neo4j". You will then be asked to change neo4j's password. Once this is done, you may need to restart neo4j.


## Quickstart:

Once you have installed, configured and initialised Neo4j, you can start POX (make sure you have an underlying network, like one emulated by Mininet)

```bash
./pox.py gox --uri="bolt://localhost:7687"
```

## Arguments

To be able to connect properly to the Neo4j database, you have to specify a few arguments:

* **uri**: address of the Neo4j database. In the previous example, "bolt" is the protocol method used to connect to Neo4j, and it can differ for you. The port may change as well.
* **username**: username for the Neo4j database. By default, GOX will consider the username to be "neo4j", like Neo4j's default user.
* **password**: password associated to the username of the Neo4j database. By default, it is "password". You should change it!

## Summary

```bash
./pox.py gox --uri="<protocol>://<ip/hostname>:<port>" --username="<username>" --password="<password>"
```

## GOX and POX with Mininet

GOX can be used with Mininet for emulating a network. For example, here is how to launch a simple tree topology with mininet:

```bash
sudo mn \
    --topo tree,depth=2,fanout=5\
    --controller=remote,ip=127.0.0.1,port=6633
```


Along with GOX on this repository are 3 topologies taken from the Internet Topology Zoo, and converted using [Sjas's "Assessing Mininet" repository](https://github.com/sjas/assessing-mininet) from a .graphml format to a Mininet python-based topology.

To use such topologies, go into the `mininet_topologies` folder, and launch Mininet with the following commande, replacing `<topology>` with the topology you want:

```bash
sudo mn \
    --custom=./renater_2010.py --topo generated \
    --controller=remote,ip=127.0.0.1,port=6633
```

# GOX applications

## GOX's L2 forwarding application

GOX is shipped with a Proof-of-Concept level 2 forwarding application which calculates the shortest path between two hosts on network. You should take a look at it if you want to develop new graph-based SDN applications using GOX.

To use it, simply copy the associated Python script from GOX's repository in the *app/* folder to POX's *ext/* directory and execute it this way:

```bash
./pox.py gox <arguments> gox_l2_forwarding
```

## Developing GOX applications

GOX allows you to develop SDN applications using a powerful graph database. The network topology is stored within this database, and applications can communicate with it for implementing new logic on the network.

GOX provides methods within the *gox_db* component for interacting with the database for very simple tasks. However, it will not be sufficient for more complexe mechanisms, so you should take a look at how to query the Neo4j database using Cypher. 

Executing GOX applications is the same as executing POX applications, so you should take a look at [POX's documentation](https://noxrepo.github.io/pox-doc/html/). 

# Troubleshooting

For POX specific issues, you may take a look at [POX's documentation](https://noxrepo.github.io/pox-doc/html/).

## The network topology stored in the database is disjoint

If you execute GOX and find by querying the database that it is disjoint in many small pieces, it may be a problem during the discovery of hosts and switches on the network.

As advised by the [POX documentation](https://noxrepo.github.io/pox-doc/html/#openflow-spanning-tree), you may use the `openflow.spanning_tree` application that will prevent flooding from switches, and wait for a complete dicovery cycle to be completed :

```
./pox.py \
    gox --uri="bolt://localhost:7687" --username="neo4j" --password="password" \
    openflow.spanning_tree --no-flood --hold-down
```

## Demonstration video

You may take a look at the following demonstration video that may help you in running GOX : https://drive.google.com/file/d/1j17PcbPBIuJd6K4Q89K0jG7lQQFyem35/view


# Acknowledgments 

I would like to thank Fetia BANNOUR and Stefania DUMBRAVA with whom I worked to create GOX.

I am also grateful to the ENSIIE engineering school in Evry, France, and all its staff for giving me the opportunity to understand SDN, graph databases and to develop GOX.

I would also like to thank the researchers behind the Gavel research paper that first studied the possibility of representing a SDN network topology in the form of a graph database. [Link to Gavel](https://github.com/engbarakat/Gavel)

# Contact

If you have any questions on GOX, how to use it, how to develop GOX applications or if you want to improve GOX, you can send me an e-mail at [alex.danduran@protonmail.com](mailto:alex.danduran@protonmail.com)

