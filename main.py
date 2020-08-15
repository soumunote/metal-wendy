import RPi.GPIO as GPIO
import time

INTERVAL = 0.15
PIN = 14
FREQ = 50

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, FREQ)

servo.start(0.0)

for i in range(10):
    servo.ChangeDutyCycle(2.5)
    time.sleep(INTERVAL)

    servo.ChangeDutyCycle(10)
    time.sleep(INTERVAL)

GPIO.cleanup()


