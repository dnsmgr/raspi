import sys, tty, termios
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


def gpio_callback(gpio_id, val):
    print("gpio %s: %s" % (gpio_id, val))

GPIO.add_interrupt_callback(forwardRight, gpio_callback)


def goForward():
 #Go fordward for one second
 GPIO.output(forwardRight,True)
 GPIO.output(forwardLeft,True)
 time.sleep(sleepSeconds)
 GPIO.output(forwardRight,False)
 GPIO.output(forwardLeft,False)

def goBackward():
 #go backward for one second

 
 GPIO.output(backwardRight,True)
 GPIO.output(backwardLeft,True)
 time.sleep(sleepSeconds)
 GPIO.output(backwardRight,False)
 GPIO.output(backwardLeft,False)

def turnRight():
 #Turn right
 GPIO.output(backwardRight,True)
 time.sleep(sleepSeconds)
 GPIO.output(backwardRight,False)

def turnLeft():
 #Turn Left
 GPIO.output(backwardLeft,True)
 time.sleep(sleepSeconds)
 GPIO.output(backwardLeft,False)

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Instructions for when the user has an interface
print("w: Go Forward")
print("s: Go Backward")
print("d: Turn Left")
print("a: Turn right")
print("x: Exit Program")

# Infinite loop that will not end until the user presses the
# exit key
while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()

    # The car will drive forward when the "w" key is pressed
    if(char == "w"):
	print("Go Forward")
        goForward()

    # The car will reverse when the "s" key is pressed
    if(char == "s"):
	print("Go Reverse")
        goBackward()
        
    # The "a" key will toggle the steering left
    if(char == "a"):
	print("Turn left")
	turnLeft()
    # The "d" key will toggle the steering right
    if(char == "d"):
        print("Turn right")
	turnRight()
    
    # The "x" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    #motor2.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""
