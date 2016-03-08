import RPi.GPIO as GPIO
import time

forwardRight = 7
forwardLeft = 15
backwardRight = 11
backwardLeft = 13
sleepSeconds = 1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(forwardRight,GPIO.OUT)
GPIO.setup(backwardRight,GPIO.OUT)
GPIO.setup(backwardLeft,GPIO.OUT)
GPIO.setup(forwardLeft,GPIO.OUT)

#Go fordward for one second

GPIO.output(forwardRight,True)
GPIO.output(forwardLeft,True)
time.sleep(sleepSeconds)
GPIO.output(forwardRight,False)
GPIO.output(forwardLeft,False)

#go backward for one second

GPIO.output(backwardRight,True)
GPIO.output(backwardLeft,True)
time.sleep(sleepSeconds)
GPIO.output(backwardRight,False)
GPIO.output(backwardLeft,False)

#Turn right
GPIO.output(backwardRight,True)
time.sleep(sleepSeconds)
GPIO.output(backwardRight,False)

#Turn Left
GPIO.output(backwardLeft,True)
time.sleep(sleepSeconds)
GPIO.output(backwardLeft,False)

GPIO.cleanup()

