from picamera import PiCamera
from os import listdir
from PIL import Image as PImage

import telebot
import time
import RPi.GPIO as GPIO

camera = PiCamera()
cameraOnline = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

bot = telebot.TeleBot("886187441:AAFmuBkGdv4bDJHYaDQVXFWaePyYQic6Eko")

cameraOnline = False

def ToggleBot():
    global cameraOnline

    while cameraOnline:
        if GPIO.input(16) == GPIO.HIGH:
            print("Motion detected...")
            camera.start_preview()
            time.sleep(0.5)
            camera.capture('/home/pi/images/image.jpg')
            bot.send_photo(chat_id=-460930897, photo=open("/home/pi/images/image.jpg", "rb"))
            camera.stop_preview()

            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.1)


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
def send_welcome(message):
    SetCameraValue(True)

@bot.message_handler(commands=['stop'])
def send_welcome(message):
	SetCameraValue(False)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Wrong Input")

GPIO.output(18,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(18,GPIO.LOW)
time.sleep(0.5)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(18,GPIO.LOW)
time.sleep(0.5)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(18,GPIO.LOW)

bot.polling()
