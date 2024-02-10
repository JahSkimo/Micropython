from machine import Pin, PWM 
import utime

color1 = PWM(Pin(14))
color1.freq(500)

color2 = PWM(Pin(15))
color2.freq(500)

for i in range(100):
    color1.duty_u16(i*245)
    color2.duty_u16((100-i)*655)
    utime.sleep_ms(100)
