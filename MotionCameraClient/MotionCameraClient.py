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

f = open("token.txt", "r")
lines = f.readlines()
token = f[0].strip()
groupId = f[1].strip()

print("Token: " + str(token))
print("GroupID: " + str(groupId))

bot = telebot.TeleBot(str(token))

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

def BlinkFast(times):
    timesBlinked = 0
    while int(timesBlinked) != int(times):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        timesBlinked = timesBlinked + 1

def BlinkSlow(times):
    timesBlinked = 0
    while int(timesBlinked) != int(times):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        timesBlinked = timesBlinked + 1

def SetCameraValue(value):
    global cameraOnline
    global botIsRunning

    cameraOnline = value

    if cameraOnline == True:
        print("Cameras online!...")
        ToggleBot()
    else:
        print("Cameras offline!...")

@bot.message_handler(commands=['start'])
def StartCamera(message):
    SetCameraValue(True)

@bot.message_handler(commands=['stop'])
def StopCamera(message):
	SetCameraValue(False)

@bot.message_handler(func=lambda message: True)
def EchoAll(message):
    bot.reply_to(message, "Wrong Input")

camera.start_preview()
BlinkFast(10)
camera.stop_preview()

bot.polling()
