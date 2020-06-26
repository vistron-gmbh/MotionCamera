#Libraries
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import telebot

#Declaration
camera = PiCamera()
pir = MotionSensor(16)
cameraOnline = False
led = LED(17)
bot = telebot.TeleBot("886187441:AAFmuBkGdv4bDJHYaDQVXFWaePyYQic6Eko")

#Settings
camera.roatation = 180
camera.start_preview()

# Überwachungsmethode
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

# Startet die Überwachung
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ToggleBot(True)

# Beendet die Überwachung
@bot.message_handler(commands=['stop'])
def send_welcome(message):
	ToggleBot(False)

# Deaktiviert die Kamera
@bot.message_handler(commands=['deactivate'])
def send_welcome(message):
	camera.stop_preview()

# Aktiviert die Kamera
@bot.message_handler(commands=['activate'])
def send_welcome(message):
	camera.start_preview()

# Fängt falsche Eingaben ab
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Wrong Input")

# Aktiviert den Bot
bot.polling()
