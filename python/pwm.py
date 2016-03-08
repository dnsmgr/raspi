import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)

p = GPIO.PWM(13,50) 
p.start(0)

for i in range(100):
	p.ChangeDutyCycle(0+i)
        time.sleep(0.02)

for i in range(100):

	p.ChangeDutyCycle(100-i)
	time.sleep(0.02)         #These three lines loop and decrease the power from 100%-1% gradually

p.stop()
GPIO.cleanup()



