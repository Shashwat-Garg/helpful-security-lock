import RPi.GPIO as GPIO
import time
def start():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    pwm = GPIO.PWM(31,50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.3)
    pwm.start(0)
    pwm.ChangeDutyCycle(70)
    time.sleep(1)
    pwm.stop()

def passAccepted():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    pwm = GPIO.PWM(31,50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.3)
    pwm.start(0)
    pwm.ChangeDutyCycle(95)
    time.sleep(1)
    pwm.stop()
    
def passRejected():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    pwm = GPIO.PWM(31,50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.3)
    for i in range(3):
        pwm.start(0)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        pwm.stop()
        time.sleep(0.3)

def blindCall():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    pwm = GPIO.PWM(31,50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.3)
    for i in range(10):
        pwm.start(0)
        pwm.ChangeDutyCycle(50)
        time.sleep(0.5)
        pwm.stop()
        time.sleep(0.3)