import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RECEIVER 	= 12
LIGHT 		= 26

GPIO.setup(RECEIVER,GPIO.IN)
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.output(LIGHT, False)

def flash(seconds):
	GPIO.output(LIGHT,True)
	time.sleep(seconds)
	GPIO.output(LIGHT,False)

time.sleep(2)
#flash(.5)

while True:
	if GPIO.input(RECEIVER)==0:
		flash(.3)
		time.sleep(.1)        
GPIO.cleanup()
