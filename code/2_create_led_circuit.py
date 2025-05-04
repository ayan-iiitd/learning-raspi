## import module connecting to raspi
from machine import Pin
from time import sleep

## define var for connecting to specific item or pin number on raspi
ledpin = Pin(15, Pin.OUT)

while True:

    ledpin.value(0)
    sleep(0.02)
    ledpin.value(1)
    sleep(0.02)