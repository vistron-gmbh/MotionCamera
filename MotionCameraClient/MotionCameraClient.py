from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from os import listdir
from PIL import Image as PImage

import telebot
import RPi.GPIO as GPIO

camera = PiCamera()
pir = MotionSensor(16)
cameraOnline = False
GPIO.setup(17,GPIO.Out)

bot = telebot.TeleBot("886187441:AAFmuBkGdv4bDJHYaDQVXFWaePyYQic6Eko")
chatID = 621572890

camera.roatation = 180
camera.start_preview()

def ToggleBot(value):
    if value == True:
        cameraOnline = True
        print("Cameras Online!..")
    else:
        cameraOnline = False
        print("Cameras Offline!..")

    while cameraOnline:
        pir.wait_for_motion()
        print("Motion detected...")
        GPIO.output(17,GPIO.HIGH)
        print("Motion detected")
        camera.capture('/home/images/image.jpg')
        img = PImage.open('/home/images/image.jpg')
        bot.send_photo(chatID, img)
        GPIO.output(17,GPIO.LOW)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    ToggleBot(True)

@bot.message_handler(commands=['stop'])
def send_welcome(message):
	ToggleBot(False)

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
