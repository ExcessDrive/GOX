#!/bin/sh

echo "INSTALLATION SCRIPT FOR GOX. MAKE SUR YOU ARE IN GOX'S DIRECTORY"

echo "[+] Installing Neo4j's debian repositories"
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list

echo "[+] Updating APT database"
sudo apt update

echo "[+] Installing neo4j-server"
sudo apt install neo4j
echo "[i] You still need to configure neo4j (/etc/neo4j/neo4j.conf)"
echo "[+] Installing neo4j pip module"
pip install neo4j

echo "[+] Installing mininet"
sudo apt install mininet

echo "[+] Cloning POX's git repository"
git clone https://github.com/noxrepo/pox.git

echo "[+] Installing GOX's applications in POX"
cp ./gox_core/* ./pox/ext/
cp ./gox_apps/* ./pox/ext/

echo "[+] All done !"
