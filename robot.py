import sys, tty, termios
import RPi.GPIO as GPIO
import time

forwardRight = 7
forwardLeft = 15
backwardRight = 11
backwardLeft = 13
sleepSeconds = 1
isRunning = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(forwardRight, GPIO.OUT)
GPIO.setup(backwardRight, GPIO.OUT)
GPIO.setup(backwardLeft, GPIO.OUT)
GPIO.setup(forwardLeft, GPIO.OUT)

GPIO.setup(forwardLeft, GPIO.OUT)


def stopRobot():
    GPIO.output(forwardRight, False)
    GPIO.output(forwardLeft, False)
    GPIO.output(backwardRight, False)
    GPIO.output(backwardLeft, False)


def goForward():
    # Go forward for one second
    GPIO.output(forwardRight, True)
    GPIO.output(forwardLeft, True)


def goBackward():
    # go backward for one second

    GPIO.output(backwardRight, True)
    GPIO.output(backwardLeft, True)


def turnRight():
    # Turn right
    GPIO.output(backwardRight, True)


def turnLeft():
    # Turn Left
    GPIO.output(backwardLeft, True)


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
print("s: Stop")
print("d: Turn right")
print("a: Turn left")
print("x: Exit Program")

# Infinite loop that will not end until the user presses the
# exit key
while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()

    if char == "s":
        print("Stop")
        stopRobot()

    if char == "w":
        print("Go Forward")
        stopRobot()
        goForward()

    if char == "r":
        print("Go Reverse")
        stopRobot()
        goBackward()

    if char == "a":
        print("Turn left")
        stopRobot()
        turnLeft()

    if char == "d":
        print("Turn right")
        stopRobot()
        turnRight()

    if char == "x":
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    # motor2.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""

GPIO.cleanup()
