## import module connecting to raspi
from machine import Pin
from time import sleep

## define var for connecting to specific item or pin number on raspi
ledpin = Pin(15, Pin.OUT)

## led starts out at off position
ledpin.off()
sleep(5)
sos = "SOS"

while True:
    
    for c in sos:
    
    ## for S led switches on for 0.5 secs and then switches off for 0.5 secs
    ## for O led switches on for 1 sec and then switches off for 0.5 secs
    
    
        print(c)
        if c == 'S':
        
            print("S LED ON 1")
            ledpin.on()
            sleep(0.5)
            ledpin.off()
            sleep(0.5)
            print("S LED ON 2")
            ledpin.on()
            sleep(0.5)
            ledpin.off()
            sleep(0.5)
            print("S LED ON 3")
            ledpin.on()
            sleep(0.5)
            ledpin.off()
            sleep(0.5)
        
        else:
            
            print("O LED ON 1")
            ledpin.on()
            sleep(1)
            ledpin.off()
            sleep(0.5)
            print("O LED ON 2")
            ledpin.on()
            sleep(1)
            ledpin.off()
            sleep(0.5)
            print("O LED ON 3")
            ledpin.on()
            sleep(1)
            ledpin.off()
            sleep(0.5)
    
    print("DONE")
    sleep(10)