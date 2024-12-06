import RPi.GPIO as UltraIO 
# import webbrowser
import time 

UltraIO.setmode(UltraIO.BCM) 

UltraIO_TRIG = 24 
UltraIO_ECHO = 18

UltraIO.setup(UltraIO_TRIG, UltraIO.OUT) 
UltraIO.setup(UltraIO_ECHO, UltraIO.IN) 

UltraIO.output(UltraIO_TRIG, UltraIO.LOW) 
time.sleep(2) 
UltraIO.output(UltraIO_TRIG, UltraIO.HIGH) 
time.sleep(0.00001) 
UltraIO.output(UltraIO_TRIG, UltraIO.LOW) 

while UltraIO.input(UltraIO_ECHO)==0: 
	start_time = time.time() 

while UltraIO.input(UltraIO_ECHO)==1: 
	Bounce_back_time = time.time() 

pulse_duration = Bounce_back_time - start_time 

distance = round(pulse_duration * 17150, 2) 

print (f"Distance: {distance} cm") 

if (distance < 20):
	print(f"The Dustbin is full and only {distance} cm is free")
	webbrowser.open('file:///home/ecobarter/templates/fullbin.html', new=0)

UltraIO.cleanup() 



# from gpiozero import DistanceSensor
# from time import sleep

# sensor = DistanceSensor(18, 24)

# while True:
    # print('Distance to nearest object is', sensor.distance, 'm')
    # sleep(1)
