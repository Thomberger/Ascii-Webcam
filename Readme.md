# ASCII Webcam

This python project output the webcam images as ascii characters. It simply add the webcam caputre to a regular ascci converting image script. You can obtain results of this kind:

 <img src="./Capture.jpg" width="70%" >

 It has been inspired [this video](https://www.youtube.com/watch?v=DBnStqiLB-Q) from the french youtuber micode

## Dependencies

 This project use [opencv](https://pypi.org/project/opencv-python/) library to capture images from the webcam and process them

## How to used

* run the script
* Put the console in full screen
* Enjoy

You may need to invert the scale (if you have console written in black over white), you can do that by adding "[::-1]" to line 22.<br>
You may want to have more grey nuances you can do that by modifying line 22 with this scale " .,:;i1tfLCG08@" (Default is  " .:-=+*#%@"). More scales can be found [here](http://paulbourke.net/dataformats/asciiart/)

## Licence

This software is distributed under the MIT license. Enjoy!
