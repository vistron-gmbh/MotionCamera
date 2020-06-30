from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import telebot

camera = PiCamera()
pir = MotionSensor(16)
cameraOnline = False
led = LED(17)
bot = telebot.TeleBot("886187441:AAFmuBkGdv4bDJHYaDQVXFWaePyYQic6Eko")

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
        led.on()
        print("Motion detected")
        camera.capture('/home/pi/Desktop/image%s.jpg' %i)
        led.off()

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
