#!/usr/bin/env python3

import pigpio
import time
from threading import Lock

GPIO_NO_LEFT  = 18
GPIO_NO_RIGHT = 19
PWM_HZ = 50
LEFT  = 1
RIGHT = 2

class WingController:
  """Wendy の耳たぶを制御する

  サーボモーター SG-90 を使用して耳たぶの制御を行う
  通常時(下) = -90, 水平 = 0, 上向 = +90 ... この角度は SG-90 を踏襲
  現在、左右耳の個別制御は行っていない

  pigpio はカプセル化せずに インスタンス化する際に与える

  GPIO18, GPIO19 を占有する
  """

  def __init__(self, pi):
    self.__lock = Lock()
    self.__pi = pi
    self.__pi.set_mode(GPIO_NO_LEFT,  pigpio.OUTPUT)
    self.__pi.set_mode(GPIO_NO_RIGHT, pigpio.OUTPUT)
    self.__degree = 90
    self.origin()

  def origin(self):
    """原点復帰
    
    原点復帰に必要な最大時間待機する
    """
    self.rotate(-90)
    time.sleep(0.36) # 0.12(s)/60(degree) 

  def rotate(self, degree:int, step:int = 0):
    """指定した角度へ回転させる

    Args:
      degree:int 回転角度(絶対角) SG-90 性能範囲外は補正をかける
      step:int 何度つづ回転させるか？(指定した場合、step毎に10msのタイマウェイトをかける)
      
    """
    # fg-90 の性能として -90°〜+90°へ補正
    if   degree >  90:
      degree =  90
    elif degree < -90:
      degree = -90
    # 現在角(self.__degree)と指定角(degree)の関係よりstepを補正
    if degree > self.__degree:
      step = abs(step)
    else:
      step = - abs(step)

    with self.__lock:

      # ループ用 step, endRange 計算 / +1 はPython range 関数の都合
      innerStep = step if step != 0 else (degree - self.__degree)  
      endRange  = degree + (1 if innerStep > 0 else -1)

      if innerStep != 0:
        # 実回転(現在位置+step 〜 指定位置 : )
        for d in range(self.__degree + innerStep, endRange, innerStep):
          self.__pi.hardware_PWM(GPIO_NO_LEFT,  PWM_HZ, self.Degree2Ratio(d, LEFT))
          self.__pi.hardware_PWM(GPIO_NO_RIGHT, PWM_HZ, self.Degree2Ratio(d, RIGHT))
          time.sleep(0.12 * abs(innerStep) / 60 + (0.01 if step !=0 else 0)) # 0.12(s)/60(degree) 
          
        self.__degree = degree

  def Degree2Ratio(self, degree, wing):
    """角度(degree)から SG-90 制御用パルスRatioを返す

    Args:
      degree(int): -90〜90 の角度範囲(下=-90, 水平=0, 上＝90)
      wing(Wing): LEFT/RIGHT ... どちらの耳か？(Wendy自身のどちらの耳か？)

    Returns：
      25000 〜 120000 Pulse Ratio(%) * 1000
      左耳は CCW で 120000 〜  25000
      右耳は CW  で　25000 〜 120000
    """
    if   wing == LEFT:
      ratio = int((120000 - 25000) * (90 - degree) / 180) + 25000
    elif wing == RIGHT:
      ratio = int((120000 - 25000) * (degree + 90) / 180) + 25000
    else:
      ratio = 0
    return ratio

def easyDemo():
  pi = pigpio.pi()
  wc = WingController(pi)
  wc.rotate(-30)
  wc.rotate(-90, 2)
  wc.rotate( 90, 4)
  wc.rotate(-90, 6)
  time.sleep(1)
  pi.stop()

def main():
  easyDemo()

if __name__ == "__main__":
  main()
