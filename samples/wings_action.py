#!/usr/bin/env python3

import pigpio
import time

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)

for i in range(1, 3):
  pi.hardware_PWM(18, 50, 25000)
  time.sleep(.2)
  pi.hardware_PWM(18, 50,120000)
  time.sleep(0.2)

pi.set_mode(18, pigpio.INPUT)
pi.stop()
