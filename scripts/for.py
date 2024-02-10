from include.rcc_library import Raft
import utime

myraft = Raft()

for i in range(12):
    myraft.led_on()
    utime.sleep_ms(200)
    myraft.led_off()
    utime.sleep_ms(500)