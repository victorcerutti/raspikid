#!/usr/bin/python

import pygame
import os, sys, time
from time import sleep

import logging

from omxplayer.player import OMXPlayer
from time import sleep


logging.basicConfig(filename='log.log',level=logging.DEBUG, format='%(asctime)s\t%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

logging.info('Media center is launched')

os.system('clear')
pygame.init()

#todo: find the ratio
#print(pygame.display.list_modes())

width = 1080
height = 720
#todo: try 1920 x 1080

#Startup sound
pygame.mixer.music.load('./sounds/startup_20.mp3')
pygame.mixer.music.play(0)


#open the files whith correspondance between barcode and movies
listing = open("./movies.txt","r")


while True:

  barcode = input("Please scan your movie barcode... ") # waiting the barcode to be scanned and sent

  logging.debug('Scanning '+barcode)

  if barcode == 'SHUTDOWN' :
    print ('Shutting down...')
    logging.info('Shutting down')
    listing.close()
    pygame.quit()
    os.system('sudo shutdown -h now')
    exit()

  elif barcode == 'EXIT' :
    print ('Exiting...')
    logging.info('Exiting')
    listing.close()
    pygame.quit()
    exit()

  elif barcode == 'PAUSE' :
    print('Pausing video...')
    logging.info('Pause')
    try:
      player.play_pause()
      print("position "+player.position()+" sec")
    except :
      print("")

  elif barcode == 'STOP' :
    print('Stopping video...')
    logging.info('Stop')
    try:
      print("position "+player.position()+" sec")
      player.quit()
    except :
      print("")

  elif barcode == '+10sec':
    try:
      player.seek(10)
    except:
      print("Error while seeking")

  elif barcode == '-10sec':
    try:
      player.seek(-10)
    except:
      print("Error while seeking")

  elif barcode == '+1min':
    try:
      player.seek(60)
    except:
      print("Error while seeking")

  elif barcode == '-1min':
    try:
      player.seek(-60)
    except:
      print("Error while seeking")

  elif barcode == '+10min':
    try:
      player.seek(600)
    except:
      print("Error while seeking")

  elif barcode == '-10min':
    try:
      player.seek(-600)
    except:
      print("Error while seeking")

  # Search the barcode in the listing
  else:

    #initialize vars
    foundMovie = False
    listing.seek(0)

    for line in listing:

      datas = line.rstrip('\n\r').split(",")

      if datas[0] == barcode :

        #./omxplayer -p -o hdmi test.mkv
        print('Playing movie '+datas[1]);

        foundMovie=True
        logging.info('Playing movie '+barcode)

        try:
          player.quit()
        except :
          print("")

        movie = ("./movies/"+datas[1])

        try:
          #OMXPlayer(movie, args='--pos 0:10:00')
          #Start position (hh:mm:ss)
          player = OMXPlayer(movie)
        except:
          print("Error while playing movie")

        #set_position


    # no available barcode
    if foundMovie == False :
      pygame.mixer.music.load('./sounds/sad_trombone.mp3')
      pygame.mixer.music.play(0)
      print('Error with barcode')


listing.close()
