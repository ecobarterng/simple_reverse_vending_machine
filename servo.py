import RPi.GPIO as ServoGPIO
from time import sleep

#pwm.start(0)

def setAngle(angle):
    ServoGPIO.setmode(ServoGPIO.BCM)
    ServoGPIO.setup(17, ServoGPIO.OUT)
    ServoGPIO.output(17, ServoGPIO.LOW)
    pwm=ServoGPIO.PWM(17, 50)

    pwm.start(0)
    duty = angle / 18 + 2
    ServoGPIO.output(17, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    ServoGPIO.output(17, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    
def can_bottle():
    
    setAngle(95)
    # sleep(2)
    # setAngle(70)
    #sleep(0.5)
    setAngle(45)
    # sleep(2)
    #setAngle(70)
    #sleep(0.5)
    setAngle(95)
        
def plastic_bottle():
    setAngle(95)
    # sleep(2)
    # setAngle(120)
    #sleep(0.5)
    setAngle(155)
    # sleep(2)
    #setAngle(110)
    #sleep(0.5)
    setAngle(95)

if __name__ == "__main__":
    can_bottle()
    plastic_bottle()
