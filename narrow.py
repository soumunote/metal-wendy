import RPi.GPIO as GPIO
import time

INTERVAL = 0.1
FREQ = 50

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)

GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, FREQ)

servo.start(0.0)

for i in range(10):
    servo.ChangeDutyCycle(2.5)
    time.sleep(INTERVAL)

    servo.ChangeDutyCycle(5)
    time.sleep(INTERVAL)

servo.ChangeDutyCycle(0)

GPIO.cleanup()
