#!/bin/sh

set -e

run() {

sudo apt-get update
sudo apt-get -y install omxplayer
sudo apt-get -y install python3-pip
#sudo apt install libsdl1.2-dev
#pip3 install pygame
sudo apt-get -y install python3-pygame


#see http://python-omxplayer-wrapper.readthedocs.io/en/latest/
sudo apt-get -y install -y libdbus-1{,-dev}
pip3 install omxplayer-wrapper

#clone and install this repository
cd ~
sudo apt-get -y install git
git clone https://github.com/victorcerutti/raspikid

#copy exemple and initiate movies.txt
mkdir raspikid/movies/
cp raspikid/exemple/BigBuckBunny.mp4 raspikid/movies/
cp raspikid/exemple/movies.txt raspikid/

#set propre font size for TV screen
sudo sed -i '/FONTFACE=/c\FONTFACE="Terminus"' /etc/default/console-setup
sudo sed -i '/FONTSIZE=/c\FONTSIZE="16x32"' /etc/default/console-setup

#launch script after boot
sed -i "/.*raspikid-launch.*/d" ~/.bashrc
echo 'cd ~/raspikid && python3 app.py #raspikid-launch' >> ~/.bashrc

}
run
