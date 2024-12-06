import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(16,GPIO.OUT)
# GPIO.output(16,GPIO.LOW)
while True:
		
	if GPIO.input(21) == True:
		print("Metal Detected")
		# GPIO.output(16, 1)
	
	else:
		print("No Metal Detected")
		# GPIO.output(16, 0)
		
	
GPIO.cleanup()
