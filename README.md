# MotionCamera
This project includes a surveillance camera system with any number of clients that can be switched on and off via a central interface. It should be possible to store recorded images on the network drive and, if necessary, to start a live stream from a targeted camera.

## Hardware components

- Raspberry Pi 3 Model B
- RPI HC-SR501 (Motion-Sensor)
- Camera Module V2
- LED (1 x Red & 1 X Yellow)
- Resitors (2 x 220Ohm)
- Cables
- Micro-SD-Card (at least class 10 with UHS-I)

## Installation

<p align="center">
  <img src="https://www.facing-south.com/img/motionCamera.jpg" width="800">
</p>


In the MitionCamera.pdf is a scetch of the build of the Raspberry-Pi with the Motion-Sensor and the Camera. Do not use other Pins on your own and build this scetch like its shown in the scetch. If you have done the installation correctly and power on the Raspberry-Pi without an image, the red LED should be one, if motion gets tracked.

## Pins

<p align="center">
  <img src="https://roboticsbackend.com/wp-content/uploads/2019/05/raspberry-pi-3-pinout.jpg" width="400">
</p>

## Software
### Operating-System
The operating system that was installed on the Pi is the Raspberry Pi OS (Raspberry Pi OS (32-bit) Lite). The image can be found here:
[Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

### Libraries/Updates
Um die in unserem Python-Script verwendeten Bibliotheken zu verwenden, müssen einige zusätzliche Pakete, sowie Updated installiert werden, dafür müssen die folgenden Befehle ausgeführt werden:

+ sudo apt update
+ sudo apt full-upgrade
+ sudo apt-get install python-picamera
+ sudo apt install python3-pip
+ pip3 install pyTelegramBotAPI
+ sudo apt-get install rpi.gpio
+ pip install Pillow
+ sudo apt-get install libopenjp2-7
+ sudo apt-get install libtiff5

### Directions
The following folders must be created:
+ /home/pi/images
+ /home/pi/github

### Download
The entire repository of the MotionCamera project can be loaded directly from Github into the "github" folder. When this step has been completed, the folder structure should look like this:

+ /home/pi/github/MotionCamera/MotionCameraClient

### Starting Software
If you are now in the file path specified under Download after downloading the project folder, you can start the bot manually with the following input:

+ python3 MotionCameraClient.py

As soon as the software is running, the command / start can be entered in the associated telegram group. Now all captured images are loaded directly into the telegram group.</br>
As soon as the Raspberry-Pi is connected to the power, it also tries to start the monitoring software automatically. As soon as the Raspberry-Pi is connected to the power, it also tries to start the monitoring software automatically. You can tell whether the monitoring software could start itself after a waiting time of approx. 1-2 minutes by the flashing yellow LED, which will flash three times.

## Usage

The cameras are controlled via the Telegram app. The following commands can be sent to the bot, provided that you are in the same group as the bot:

| Command        | Function                   |
| -------------  | -------------------------- |
| /start         | Starts the survaillance    |
| /end           | Ends the survaillance      |

As soon as the motion detector detects movement, the red LED lights up. As soon as a photo has been taken, the yellow LED starts to flash. The motion sensor needs about 6 seconds after each movement to be able to react to the next movement. During this time the yellow LED flashes slowly. As soon as the motion sensor is ready to record the next motion, the yellow LED flashes three times in quick succession.
