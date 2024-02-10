from include.rcc_library import Raft
import utime
#Jah 1/20/24 making them blink
myraft = Raft()

myraft.led_on()
utime.sleep_ms(1000)
myraft.led_off()

myraft.led_on()
utime.sleep_ms(1000)
myraft.led_off()