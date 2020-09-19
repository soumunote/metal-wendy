#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import time

import pigpio
import wingAction
import legAction

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

pi = pigpio.pi()
wc = wingAction.WingController(pi)
lc = legAction.LegController(pi)

@app.get("/")
async def root(request: Request):
  return templates.TemplateResponse("index.html", 
    {"request": request}
  )

@app.get("/wings/single/{degree}/{step}")
async def wings_single(degree: int, step: int = 0):
  wc.rotate(degree, step)
  return {"message": "Hello World"}

@app.get("/wings/array/")
async def wings_array(degree: int):
  return {"message": "Hello World"}
  
@app.get("/wings/action/{name}")
async def wings_action(name: str):
  if name == "delight":
    """歓喜"""
    wc.rotate(15)
    time.sleep(0.7)
    for i in range(5):
      wc.rotate(-15)
      wc.rotate(15)
    wc.rotate(-90)

  elif name == "sleepy":
    """眠い"""
    wc.rotate(20, 2)
    wc.rotate(-90, 2)

  return {"message": name}

@app.get("/legs/manual/{left}/{right}")
async def legs_manual(left: int, right: int)


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
  