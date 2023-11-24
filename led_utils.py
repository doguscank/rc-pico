import machine
import time

LED = machine.Pin("LED", machine.Pin.OUT)

def blink():
    LED.on()
    time.sleep(1)
    LED.off()
    
def set_led_state(state):
    if state:
        LED.on()
    else:
        LED.off()