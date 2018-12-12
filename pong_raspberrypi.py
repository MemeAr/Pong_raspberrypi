from sense_hat import SenseHat
sense = SenseHat()

import time
import random

sense.clear(0,0,0)

purple = (150, 117, 175)
blue = (0, 249, 182)

x = random.randint(1, 6)
y = random.randint(1, 6)

x_sens = 1
y_sens = 1

rx = 0
ry = 0

ry_sens = 1

def pongRaquette():
  sense.set_pixel(rx, ry, blue)
  sense.set_pixel(rx, ry_sens, blue)
  sense.set_pixel(rx, ry_sens + 1, blue)


sense.set_pixel(x, y, purple)

while True:
  sense.clear(0,0,0)
  pongRaquette()
  sense.set_pixel(x, y, purple)
  time.sleep(0.2)
  x = x + x_sens
  y = y + y_sens
  
  if x==7:
    x_sens = -1
    
  if y==0:
    y_sens = 1

  if y==7:
    y_sens = -1
    
  if x==1 and y==ry:
    x_sens = 1
    
  if x==1 and y==ry_sens:
    x_sens = 1
  
  if x==1 and y==ry_sens+1:
    x_sens = 1
  
  if x==1 and y==ry_sens+2:
    x_sens = 1  
    
  if x==0:
    sense.clear(0,0,0)
    sense.set_pixel(x, y, 255, 0, 0)
    pongRaquette()
    break
    
  

    
  

  