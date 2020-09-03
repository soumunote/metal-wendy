#!/usr/bin/env python3

import pigpio
import time

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(19, pigpio.OUTPUT)

pi.hardware_PWM(19, 50,120000)

for i in range(1, 6):
  pi.hardware_PWM(18, 50, 72500)
  pi.hardware_PWM(19, 50, 72500)
  #pi.hardware_PWM(18, 50, 25000)
  #pi.hardware_PWM(19, 50,120000)
  time.sleep(0.3)
  pi.hardware_PWM(18, 50,120000)
  pi.hardware_PWM(19, 50, 25000)
  time.sleep(1)

pi.set_mode(18, pigpio.INPUT)
pi.set_mode(12, pigpio.INPUT)
pi.stop()
