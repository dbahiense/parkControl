#-----------------------------------
# Name: ParkingControl.py
# Created: 12/01/2016
# Creator: D.Bahiense
# Changed: 12/03/2016
#-----------------------------------
#!/usr/bin/env python

# import required libraries
import RPi.GPIO as GPIO
import time

# use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# set warnings to false
# when in production
GPIO.setwarnings(False)

# declare pins that are in use
pins = [17,18,27,22]

# set all used pins as output
for pin in pins:
  print "Setting pin %i..." %(pin)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

# set initial step = 0
step = 0
# set total steps for back and foward
# 128 steps = 90 grads
steps = 128

# backwards positions
bpos0 = [0,0,0,1]
bpos1 = [0,0,1,0]
bpos2 = [0,1,0,0]
bpos3 = [1,0,0,0]

# foward positions
fpos0 = [1,0,0,0]
fpos1 = [0,1,0,0]
fpos2 = [0,0,1,0]
fpos3 = [0,0,0,1]

# delay between steps
delay = 0.0005

# backwards / open gate
while step <= steps:
  for i in range(0,4):
    GPIO.output(pins[i],bpos0[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],bpos1[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],bpos2[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],bpos3[i])
    time.sleep(delay)
# next step
  step += 1

# after opening the gate, reset step to zero
step = 0

# TODO: check with infra red sensor if car passed through the gate already
time.sleep(2)

# foward / close gate
while step <= steps:
  for i in range(0,4):
    GPIO.output(pins[i],fpos0[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],fpos1[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],fpos2[i])
    time.sleep(delay)
  for i in range(0,4):
    GPIO.output(pins[i],fpos3[i])
    time.sleep(delay)
# next step
  step += 1

# turn off pin
GPIO.output(pins[3],0)

print "EOF"