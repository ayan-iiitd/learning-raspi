## import module connecting to raspi
from machine import Pin
from time import sleep

## define var for connecting to specific item or pin number on raspi
ledpin12 = Pin(12, Pin.OUT)
ledpin13 = Pin(13, Pin.OUT)
ledpin14 = Pin(14, Pin.OUT)
ledpin15 = Pin(15, Pin.OUT)
ledpins = [ledpin12, ledpin13, ledpin14, ledpin15]

## led starts out at off position
for ledpin in ledpins:
    ledpin.off()
sleep(5)

## test if all circuit works
# for ledpin in ledpins:
#     ledpin.on()
#     sleep(2)

while True:

    for i in range(16):
        
        print("in integer: ", i)

        ## calculate binary value on integer

        rem = 0
        quo = 0
        div = i
        binary = [0, 0, 0, 0]

        for j in range(3, -1, -1):

            quo = int(div/2)
            rem = int(div%2)
            binary[j] = rem
            div = quo

        print("in binary: ", binary)

        ## binary values represent the led value

        for j in range(3, -1, -1):
            ledpins[j].value(binary[3 - j])
        
        sleep(0.5)