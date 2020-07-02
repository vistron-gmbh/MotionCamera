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
chatID = 621572890

cameraOnline = false

def ToggleBot():
    global cameraOnline
    while cameraOnline:
        if GPIO.input(16) == GPIO.HIGH:
            print("Motion detected...")
            camera.start_preview()
            camera.capture('/home/pi/images/image.jpg')
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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global cameraOnline
    cameraOnline = true
    print("Cameras online!...")
    ToggleBot()

@bot.message_handler(commands=['stop'])
def send_welcome(message):
    global cameraOnline
    cameraOnline = false
    print("Cameras offline!...")
	ToggleBot()

@bot.message_handler(commands=['deactivate'])
def send_welcome(message):
	camera.stop_preview()

@bot.message_handler(commands=['activate'])
def send_welcome(message):
	camera.start_preview()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Wrong Input")

bot.polling()
print("Bot ready...")
