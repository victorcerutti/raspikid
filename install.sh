sudo apt-get install omxplayer
sudo apt-get install python3-pip
#sudo apt install libsdl1.2-dev
#pip3 install pygame
sudo apt-get install python3-pygame


#see http://python-omxplayer-wrapper.readthedocs.io/en/latest/
sudo apt-get install -y libdbus-1{,-dev}
pip3 install omxplayer-wrapper

#clone and install this repository
cd ~
git clone https://github.com/victorcerutti/raspikid

#copy exemple and initiate movies.txt
cp raspikid/exemple/BigBuckBunny.mp4 raspikid/movies/
cp raspikid/exemple/movies.txt raspikid/

#launch script after boot
sed -i "/.*raspikid-launch.*/d" ~/.bashrc
echo 'cd ~/raspikid && python3 app.py #raspikid-launch' >> ~/.bashrc
