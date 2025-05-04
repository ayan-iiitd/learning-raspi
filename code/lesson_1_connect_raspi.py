## import module connecting to raspi
from machine import Pin
from time import sleep

## define var for connecting to specific item or pin on raspi
raspicw_led = Pin('LED', Pin.OUT)

## LEDs can be switched on/of via the following methods
#### .on()
#### .off()
#### .toggle()
#### .value(0)
#### .value(1)


while True:
    raspicw_led.value(0)
    sleep(0.02)
    raspicw_led.value(1)
    sleep(0.02)