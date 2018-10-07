
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

# How to install
Follow raspbian installation.
After a fresh install, run boostrap.sh

# How to
1. Add movies to the movies directory (ex: BigBuckBunny.mp4)
2. Reference the with a short code (used for the barcode) in movies.txt (ex: BUNNY)
3. Generate the barcode with an online generator (ex: https://barcode.tec-it.com/en/Code128?data=BUNNY)
4. Save and print the image. Be creative !
5. It should now work !

# Usage
The program should start after booting the raspberry.
You can use simple barcode command as input to PAUSE or STOP the movie.
You can also send SHUTDOWN to close the app and shut the pi down.

# Credits

Logo crafted from icons made by [Freepik](http://www.freepik.com) from [Flaticon](https://www.flaticon.com)

[Big Buck Bunny](https://peach.blender.org/) is licensed under the
[Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/).
(c) copyright 2008, Blender Foundation / www.bigbuckbunny.org
