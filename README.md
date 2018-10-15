
![raspikid](https://raw.githubusercontent.com/victorcerutti/raspikid/master/raspikid.png)

# :heavy_exclamation_mark: Important notice
This is still alpha. It may work but still need some work and debug.

The documentation is only a draft at this time.

If you feel adventurous, don't hesitate to play and contribute.

# What is it ?
Raspikid is a simple python script that plays video on a raspberry pi.

Input is made via a barcode scanner to play media displayed on a paper card or to prompt some command (pause, stop, …)

This allow a young child to have an easily portable media player that can connect to any HDMI screen to play his favorite cartoons.

# Why ?
- autonomous usage
- physical content of media
- easy usage control for parents
- may develop will to learn how to hack it
- distraction free (no ads, no push of other content like youtube/netflix)

# How to install
>You will need of course a raspberry, a micro SD card and a barcode reader (I use [this one](https://www.amazon.fr/Proster-Lecteur-Code-Barres-Scanner-Automatique/dp/B00Y83TXOE/))
1. Download raspbian lite and follow the installation guide [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
2. If you need to activate SSH and configure wifi, follow [this instructions](https://www.raspberrypi.org/forums/viewtopic.php?t=191252).
3. After a fresh install, boot the rasppberry, and either connect it to a screen+keyboard or via SSH.
4. Run the following command. This will install raspikid.
```
curl -sL https://victorcerutti.github.io/raspikid/install.sh | sh
```

# How to configure (parents)
1. Add movies to the movies directory (ex: BigBuckBunny.mp4)
2. Reference them with a short code (used for the barcode) in movies.txt (ex: BUNNY)
3. Generate the barcode with an online generator (ex: https://barcode.tec-it.com/en/Code128?data=BUNNY)
4. Save and print the image. Be creative !
5. Also print some simple PAUSE, STOP and SHUTDOWN barcode (TODO: provide them)
5. It should now work !

# How to use it (children)
1. The program should start after booting the raspberry.
2. Just scan a barcode to start playing the video.
3. If needed, you can scan PAUSE or STOP to control the playback.
4. When you are done, scan SHUTDOWN to close the app and shut the pi down.

# Next steps / Contributions
If you want to contribute, you are more than welcome. Write an issue if needed or just fork and submit a PR.

This are the next goal to achieve, no particular order :
- smart logs (number of plays, video time…)
- parental control (limit to a certain time per day)
- REST api for distant control (stop, pause, ability to block)
- integrate with [Home Assistant](https://www.home-assistant.io/) as a media player

# Credits

Logo crafted from icons made by [Freepik](http://www.freepik.com) from [Flaticon](https://www.flaticon.com)

[Big Buck Bunny](https://peach.blender.org/) is licensed under the
[Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/).
(c) copyright 2008, Blender Foundation / www.bigbuckbunny.org
