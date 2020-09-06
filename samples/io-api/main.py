#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI

import pigpio
from wings-action import WingController

app = FastAPI()
pi = pigpio.pi
wc = WingController(pi)

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/wings/single/{degree}/{step}")
async def wings_single(degree: int, step: int):
  return {"message": "Hello World"}

@app.get("/wings/array/")
async def wings_array(degree: int):
  return {"message": "Hello World"}
  
@app.get("/wings/action/{name}")
async def wings_action(name: str):
  wc = WingController()
  wc.
  return {"message": name}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
  