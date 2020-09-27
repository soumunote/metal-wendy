# ハードウェア
## Raspberry PI 電源制御/監視[rpi-power]
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

## Raspberry PI ピン結線
```
                    ┏━━━━━━━━━━━━━┳━━┳━━┳━━━━━━━━━━━━━━┓  
   VCC DRV8835(12) ─┨     3.3V    ┃ 1┃ 2┃5.0V          ┃  
                    ┃I2C  GPIO 2  ┃ 3┃ 4┃5.0V          ┃  
                    ┃I2C  GPIO 3  ┃ 5┃ 6┃GND           ┠─ board GND 
                    ┃     GPIO 4  ┃ 7┃ 6┃GPIO 14       ┃  
                    ┃     GND     ┃ 9┃10┃GPIO 15       ┃  Servo (orange)
                    ┃     GPIO 17 ┃11┃12┃GPIO 18  PWM0 ┠─ Left Wing 
                    ┃     GPIO 27 ┃13┃14┃GND           ┃  
                    ┃     GPIO 22 ┃15┃16┃GPIO 23       ┠─ DRV8835(8) BIN1/BPHASE
                    ┃     3.3V    ┃17┃18┃GPIO 24       ┃  
                    ┃     GPIO 10 ┃19┃20┃GND           ┃  
                    ┃     GPIO 9  ┃21┃22┃GPIO 25       ┠─ DRV8835(7) BIN2/BENABLE
                    ┃     GPIO 11 ┃23┃24┃GPIO 8        ┃  
                    ┃     GND     ┃25┃26┃GPIO 7        ┃  
                    ┃     ID_SD   ┃27┃28┃ID_SC         ┃  
                    ┃     GPIO 5  ┃29┃30┃GND           ┃  
                    ┃     GPIO 6  ┃31┃32┃GPIO 12  PWM0 ┃  
    Right Wing      ┃PWM1 GPIO 13 ┃33┃34┃GND           ┃  
    Servo (orange) ─┨PWM1 GPIO 19 ┃35┃36┃GPIO 16       ┃  
                    ┃     GPIO 26 ┃37┃38┃GPIO 20       ┠─ DRV8835(10) AIN1/APHASE
                    ┃     GND     ┃39┃40┃GPIO 21       ┠─ DRV8835(9)  AIN2/AENABLE
                    ┗━━━━━━━━━━━━━┻━━┻━━┻━━━━━━━━━━━━━━┛  
```

## SG90 制御概要
### 回転角度
- シグナル特性  
  [秋月電子通商データシートからの抜粋](http://akizukidenshi.com/catalog/g/gM-08761/)  
  ![シグナル特性](image/sg90-signal.png)  

- 実物  
　![実物](image/sg90.png)
  - 裏から見て CW 方向

- 角度の計算
  | -90° | 0° | +90° | 備考 |
  |:--:|:--:|:--:|:--:|
  | 0.5ms plus | 1.45 plus | 2.4 plus | データシートより |
  | 0.5 / 20 | 1.45 / 20 | 2.4 / 20 | 20ms PWM Period |
  | 2.5 | 7.25 | 12 | % |

## DRV8835 及び DCモーター結線
```
┏━━━━━━━━┓ Yellow 
┃DC Left ┠───────────┐   ┏━━━━━━━━━━━━┳━━┳━━┳━━━━━━━━━━━━┓
┃        ┠──────────┐│   ┃          VM┃ 1┃12┃VCC         ┃
┗━━━━━━━━┛ Green    │└───┨       AOUT1┃ 2┃11┃MODE        ┃
                    └────┨       AOUT2┃ 3┃10┃AIN1/APHASE ┃
                    ┌────┨       BOUT1┃ 4┃ 9┃AIN2/AENABLE┃
┏━━━━━━━━┓ Purple   │┌───┨       BOUT2┃ 5┃ 8┃BIN1/BPHASE ┃
┃DC Right┠──────────┘│   ┃         GND┃ 6┃ 7┃BIN2/BENABLE┃
┃        ┠───────────┘   ┗━━━━━━━━━━━━┻━━┻━━┻━━━━━━━━━━━━┛  
┗━━━━━━━━┛ Blue
```

## スライドパッドの傾きとDCモーターの駆動関係
```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Left  Right        ┃        Left  Right ┃
┃ |y|   r            ┃        r     |y|   ┃
┃                    ┃                    ┃
┃           (-1, -1) ┃ (+1, -1)           ┃
┣━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━┫
┃           (-1, +1) ┃ (+1, +1)           ┃
┃                    ┃                    ┃
┃ Left  Right        ┃        Left  Right ┃
┃ -|y|  -r           ┃        -r    -|y|  ┃
┗━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┛ 
```

