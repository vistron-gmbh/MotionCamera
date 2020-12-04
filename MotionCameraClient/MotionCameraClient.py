from picamera import PiCamera
from os import listdir
from PIL import Image as PImage

import time
import telebot
import RPi.GPIO as GPIO

camera = PiCamera()
cameraOnline = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

# read the telegram token and the group id from the token.txt
f = open("token.txt", "r")
lines = f.readlines()
token = lines[0].strip()
groupId = lines[1].strip()

print("Token: " + str(token))
print("GroupID: " + str(groupId))

# initialize the telegram bot
bot = telebot.TeleBot(str(token))

# starts the monitoring of the motion sensor and sends an image if the motion sensor reacts
def ToggleBot():
    global cameraOnline

    while cameraOnline:
        if GPIO.input(16) == GPIO.HIGH:
            print("Motion detected...")
            camera.start_preview()
            time.sleep(0.5)
            camera.capture('/home/pi/images/image.jpg')
            bot.send_photo(chat_id=int(groupId), photo=open("/home/pi/images/image.jpg", "rb"))
            camera.stop_preview()
            BlinkSlow(6)
            BlinkSlow(3)

# let the led blink fast
def BlinkFast(times):
    timesBlinked = 0
    while int(timesBlinked) != int(times):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        timesBlinked = timesBlinked + 1

# let the led blink slow
def BlinkSlow(times):
    timesBlinked = 0
    while int(timesBlinked) != int(times):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        timesBlinked = timesBlinked + 1

# initializes the camera and starts the monitoring if camera is online
def SetCameraValue(value):
    global cameraOnline
    global botIsRunning

    cameraOnline = value

    if cameraOnline == True:
        print("Cameras online!...")
        ToggleBot()
    else:
        print("Cameras offline!...")

# command from telegram to start the monitoring
@bot.message_handler(commands=['start'])
def StartCamera(message):
    SetCameraValue(True)

# command from telegram to stop the monitoring
@bot.message_handler(commands=['stop'])
def StopCamera(message):
	SetCameraValue(False)

# bot responds to the input of the user
@bot.message_handler(func=lambda message: True)
def EchoAll(message):
    bot.reply_to(message, "Wrong Input")

camera.start_preview()
BlinkFast(10)
camera.stop_preview()

bot.polling()
