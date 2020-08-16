# metal-wendy

## GPIOツール
- pinout  
  [Gpiozero Command Line Tool](https://gpiozero.readthedocs.io/en/stable/cli_tools.html?highlight=pinout#pinout)  
  [Installing GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html)  
  ```sh
  sudo apt install python3-gpiozero
  ```
  (Python3でないとダメだった。)

- Wiring Pi  
  [Wiring Pi](http://wiringpi.com/download-and-install/)  

## 電源制御/監視
現在のOSの動作状態を知る術が無い。(USB-WiFiのLEDで辛うじて起動中であることを知ることはできる。)
- OSのシャットダウンを物理ボタンで行う  
  /boot/config.txt に以下の記述を追加することで、GPIOがHIGHになった際にshutdownを行うことが可能
  ```
  dtoverlay=gpio-shutdown,gpio_pin=10
  ```
  BCM=19, BOARD=19 が HIGH でシャットダウン

- OSが起動している場合、標準のグリーンLEDを点滅させる。(通常SDカードアクセス時に点灯)  
  /boot/config.txt に以下の記述を追加する
  ```
  dtparam=act_led_trigger=heartbeat
  ```
