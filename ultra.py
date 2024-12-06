import RPi.GPIO as UltraI 
import time
import pressure

# I called the pressure method here to get a value and included it in an argument 
# so the system can reject overweight items

pressureValue = pressure.getPressure() 

def measure():
	UltraI.setmode(UltraI.BCM)
	UltraI_TRIG = 27
	UltraI_ECHO = 4
	UltraI.setup(UltraI_TRIG, UltraI.OUT)
	UltraI.setup(UltraI_ECHO, UltraI.IN) 
	UltraI.output(UltraI_TRIG, UltraI.LOW)
	time.sleep(2)
	UltraI.output(UltraI_TRIG, UltraI.HIGH)
	time.sleep(0.00001)
	UltraI.output(UltraI_TRIG, UltraI.LOW)
	while UltraI.input(UltraI_ECHO)==0:
		start_time = time.time()
		
	while UltraI.input(UltraI_ECHO)==1:
		Bounce_back_time = time.time()
		
	pulse_duration = Bounce_back_time - start_time
	distance = round(pulse_duration * 17150, 2)
	print (f"Distance: {distance} cm") 

	if pressureValue > 500:
		print("Overweight Item detected")
		weight = 100
		return weight

	if distance >11 and distance <= 13:
		print("4cm can weighs 13g")
		weight = 13
		return weight
		
	elif distance > 7 and distance < 9:
		print("large ragolis and weighs 26g")
		weight = 26
		return weight
		
	elif distance > 9 and distance < 11:
		print("can and weighs 10g")
		weight = 10
		return weight
		
	elif distance >14:
		print("No item detected")
		weight = 0
		return weight
	
	weight = 100
	return weight

measure()

UltraI.cleanup() 

