from sense_hat import SenseHat
sense = SenseHat()
import time #importer le time#

sense.clear(0,0,0)

purple = (150, 117, 175)
x = 0
y = 6

sense.set_pixel(x, y, purple) #Affiché une led#

while x<7: #Faire bouger la led sur la ligne#
  sense.clear(0,0,0)
  sense.set_pixel(x, y, purple)
  time.sleep(0.5) #temps#
  x = x+1
  