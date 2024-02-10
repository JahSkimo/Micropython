from machine import Pin 

#setup input pin
input_pin = Pin(4, Pin.IN, Pin.PULL_UP)
output_pin = Pin(3, Pin.OUT)
output_pin.value(1)

while True:
    print(input_pin.value(), output_pin.value())