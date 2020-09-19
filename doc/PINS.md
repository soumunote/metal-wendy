# ピン結線

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
