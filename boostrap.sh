sudo apt-get install omxplayer
sudo apt-get install python3-pip
#sudo apt install libsdl1.2-dev
#pip3 install pygame
sudo apt-get install python3-pygame


#see http://python-omxplayer-wrapper.readthedocs.io/en/latest/
sudo apt-get install -y libdbus-1{,-dev}
pip3 install omxplayer-wrapper

#launch script after boot
sed -i "/.*raspikid-launch.*/d" ~/.bashrc
echo 'cd ~/raspikid && python3 app.py #raspikid-launch' >> ~/.bashrc
