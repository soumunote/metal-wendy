# ピン結線

```
┏━━━━━━━━━━━━━━━━━━┳━━┳━━┳━━━━━━━━━━━━━━━━━━┓  
┃          3.3V PWR┃ 1┃ 2┃5.0V PWR          ┃  
┃I2CI SDA  GPIO 2  ┃ 3┃ 4┃5.0V PWR          ┃  
┃I2C1 SCL  GPIO 3  ┃ 5┃ 6┃GND               ┃  
┃          GPIO 4  ┃ 7┃ 6┃UARTO TX          ┃  
┃          GND     ┃ 9┃10┃UARTO RX          ┃  
┃          GPIO 17 ┃11┃12┃GPIO 18           ┃  
┃          GPIO 27 ┃13┃14┃GND               ┃  
┃          GPIO 22 ┃15┃16┃GPIO 23           ┃  
┃          3.3V PWR┃17┃18┃GPIO 24           ┃  
┃SPIO MOSI GPIO 10 ┃19┃20┃GND               ┃  
┃SPIO MISO GPIO 9  ┃21┃22┃GPIO 25           ┃  
┃SPIO SCLK GPIO 11 ┃23┃24┃GPIO 8   SPIO CS0 ┃  
┃          GND     ┃25┃26┃GPIO 7   SPIO CS1 ┃  
┃          Reserved┃27┃28┃Reserved          ┃  
┃          GPIO 5  ┃29┃30┃GND               ┃  
┃          GPIO 6  ┃31┃32┃GPIO 12           ┃  
┃          GPIO 13 ┃33┃34┃GND               ┃  
┃SPI1 MISO GPIO 19 ┃35┃36┃GPIO 16  SPI1 CS0 ┃  
┃          GPIO 26 ┃37┃38┃GND      SPI1 MOSI┃  
┃          GND     ┃39┃40┃GND      SPI1 SCLK┃  
┗━━━━━━━━━━━━━━━━━━┻━━┻━━┻━━━━━━━━━━━━━━━━━━┛  
```
