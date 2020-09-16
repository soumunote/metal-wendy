# pipgpio によるハードウェア PWM により、SG-90 を制御する
## パッケージのインストール
```sh
sudo apt -y install pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpio
sudo apt -y install python-pip python3-pip
sudo pip3 install pigpio
```
## ハードウェア PWM サンプル
```python3
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
```
