#!/bin/bash

sudo apt -y update 
sudo apt -y install python3 python3-pip
pip3 install fastapi uvicorn aiofiles pigpio jinja2

sudo cp -p wendy-io-api.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start wendy-io-api
sudo systemctl enable wendy-io-api