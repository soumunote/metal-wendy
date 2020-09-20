#!/usr/bin/env python3

import pigpio
import time
from threading import Lock

GPIO_NO_LEFT_F = 20
GPIO_NO_LEFT_R = 21
GPIO_NO_RIGHT_F = 23
GPIO_NO_RIGHT_R = 25
PWM_HZ = 50
MAX_DUTYCYCLE = 255

class LegController:
  """Wendy の足回りを制御する

  pigpio はカプセル化せずに インスタンス化する際に与える
  """

  def __init__(self, pi):
    self.__lock = Lock()
    self.__pi = pi
    self.__pi.set_mode(GPIO_NO_LEFT_F,  pigpio.OUTPUT)
    self.__pi.set_mode(GPIO_NO_LEFT_R,  pigpio.OUTPUT)
    self.__pi.set_mode(GPIO_NO_RIGHT_F, pigpio.OUTPUT)
    self.__pi.set_mode(GPIO_NO_RIGHT_R, pigpio.OUTPUT)
    self.__pi.set_PWM_frequency(GPIO_NO_LEFT_F,  100)
    self.__pi.set_PWM_frequency(GPIO_NO_LEFT_R,  100)
    self.__pi.set_PWM_frequency(GPIO_NO_RIGHT_F, 100)
    self.__pi.set_PWM_frequency(GPIO_NO_RIGHT_R, 100)

  def run(self, leftSpeed, rightSpeed):
    self.left(leftSpeed)
    self.right(rightSpeed)

  def left(self, speed):
    if   speed > 0: 
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_R, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_F, speed)
    elif speed < 0:
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_F, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_R, -speed)
    else:
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_F, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_R, 0)

  def right(self, speed):
    if   speed > 0: 
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, speed)
    elif speed < 0:
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, -speed)
    else:
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, 0)
      self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, 0)

  def leftBreak(self):
    self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_F, MAX_DUTYCYCLE)
    self.__pi.set_PWM_dutycycle(GPIO_NO_LEFT_R, MAX_DUTYCYCLE)

  def rightBreak(self):
    self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, MAX_DUTYCYCLE)
    self.__pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, MAX_DUTYCYCLE)

def easyDemo():
  pi = pigpio.pi()
  lc = LegController(pi)

  pi.set_PWM_frequency(GPIO_NO_LEFT_F,  50)
  pi.set_PWM_frequency(GPIO_NO_LEFT_R,  50)
  pi.set_PWM_frequency(GPIO_NO_RIGHT_F, 50)
  pi.set_PWM_frequency(GPIO_NO_RIGHT_R, 50)

  pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F,  100)
  #pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, 255)
  time.sleep(0.5)
  pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F,  0)
  #pi.set_PWM_dutycycle(GPIO_NO_RIGHT_F, 0)
  #time.sleep(1)
  #pi.set_PWM_dutycycle(GPIO_NO_LEFT_R,  128)
  #pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, 128)
  #time.sleep(6)  
  #pi.set_PWM_dutycycle(GPIO_NO_LEFT_R,  0)
  #pi.set_PWM_dutycycle(GPIO_NO_RIGHT_R, 0)
  #time.sleep(1)
  
  pi.stop()

def main():
  easyDemo()

if __name__ == "__main__":
  main()
