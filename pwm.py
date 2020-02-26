import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pin=[12,15,16,35]
GPIO.setup(pin,GPIO.OUT)
GPIO.output(12,0)
GPIO.output(15,1)
GPIO.output(16,1)
GPIO.output(35,0)

GPIO.cleanup()



