#!/usr/bin/env python3

import pigpio
import time
from enum import Enum

class WingController:

  GPIO_NO_LEFT  = 18
  GPIO_NO_RIGHT = 19
  PWM_HZ = 50
  LEFT  = 1
  RIGHT = 2

  def __init__(self, pi):
    self.pi = pi
    self.pi.set_mode(self.GPIO_NO_LEFT,  pigpio.OUTPUT)
    self.pi.set_mode(self.GPIO_NO_RIGHT, pigpio.OUTPUT)
    self.origin()

  def origin(self):
    self.degree = -90
    self.action(-90)
    time.sleep(0.36) # 0.12(s)/60(degree) 

  def action(self, degree):
    self.pi.hardware_PWM(self.GPIO_NO_LEFT,  self.PWM_HZ, self.Degree2Ratio(degree, self.LEFT))
    self.pi.hardware_PWM(self.GPIO_NO_RIGHT, self.PWM_HZ, self.Degree2Ratio(degree, self.RIGHT))
    deltaDegree = abs(degree - self.degree)
    time.sleep(0.12 * deltaDegree / 60)
    self.degree = degree

  def Degree2Ratio(self, degree, wing):
    """
    角度(degree)から SG-90 制御用パルスRatioを返す

    Args:
      degree(int): -90〜90 の角度範囲(下=-90, 水平=0, 上＝90)
      wing(Wing): LEFT/RIGHT ... どちらの耳か？(Wendy自身のどちらの耳か？)

    Returns：
      25000 〜 120000 Pulse Ratio(%) * 1000
      左耳は CCW で 120000 〜  25000
      右耳は CW  で　25000 〜 120000
    """
    if   wing == self.LEFT:
      ratio = int((120000 - 25000) * (90 - degree) / 180) + 25000
    elif wing == self.RIGHT:
      ratio = int((120000 - 25000) * (degree + 90) / 180) + 25000
    else:
      ratio = 0
    return ratio

def easyDemo():
  pi = pigpio.pi()
  wc = WingController(pi)
  wc.action(-30)
  wc.action(-90)
  wc.action(90)
  wc.action(-90)
  for i in range(-90, 90, 12):
    wc.action(i)
    time.sleep(0.01)
  wc.action(-90)
  for i in range(-90, 90, 2):
    wc.action(i)
    time.sleep(0.01)
  wc.action(-90)
  pi.stop()

def main():
  easyDemo()

if __name__ == "__main__":
  main()
