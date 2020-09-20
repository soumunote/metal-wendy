# pipgpio によるハードウェア PWM により、SG-90 を制御する
## パッケージのインストール
```sh
sudo apt -y install pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpio
sudo apt -y install python-pip python3-pip
sudo pip3 install pigpio
pip3 install fastapi uvicorn aiofiles
