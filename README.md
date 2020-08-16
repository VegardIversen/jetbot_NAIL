# Jetbot_NAIL
Demo for jetbot, with jetson nano. 
Using [TSM Online Hand Gesture Recognition Demo](https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo) to controll between different AI-demos on the jetbot.



## Getting Started

This demo uses the SparkFun JetBot AI Kit, follow the instruction on this site: * [Sparkfun](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit/all)
It also needs a internet connection, monitor, keyboard, mouse, bluetooth speaker and a USB webcamera. Also connect the speaker to the jetson nano when connected to a monitor. 
I used a logitech hd c525 webcamera, and a JBL Go speaker. 
### Prerequisites

What things you need to install the software and how to install them
After installing the image from the Sparkfun website (if you buy the kit, it comes with a already installed image), install the necesssary packages.

These installtion can take a long while. Make sure you have a big swap-file. 

For the hand gesture recognition, follow the instruction from [mit-han-lab](https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo) online demo.
This will make a folder with the necessities, switch out the main.py with the main.py file this github and add the rest of the pythonfiles in the online_demo folder.

This needs OpenCV 4.X, wich can be install from here [JetsonHacksNano](https://github.com/JetsonHacksNano/buildOpenCV) or here [mdegans](https://github.com/mdegans/nano_build_opencv), here version 4.3.0 is used.

A new version of PyTorch is also necessary, follow the instruction from [Nvidia forum](https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-6-0-now-available/72048), pay attention that the torch version matches CUDA version, and torchvision version.
I used, PyTorch version 1.1.0, torcvision version 0.2.2

Install the requirements.txt file
```
pip3 install requirements.txt
```




## Running the tests

Go into the the online_demo folder. Run 
```
python3 main.py
```
and listen for the instruction, make sure the speaker is connected, if not the instruction will be printed to the terminal.

First select language:
thumb up for Norwegian and down for english

Start by squeezing indexfinger and thumb together like a zoom out on a smartphone. This will start program selecter. Swipe left or rigth with a open hand to switch between programs. It can sometime double switch, so watch out for that. 
thumb up to select a program, each program will run for a set amount of time before ending.
To quit program selecter show thumb down. Example for hand gestures is shown in the [TSM Online Hand Gesture Recognition Demo](https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo).


## Built With

* [TSM Online Hand Gesture Recognition Demo](https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo)
* [OpenCV](https://opencv.org/)


## Acknowledgments

* mit-han-lab
*JetsonHacksNano
*


