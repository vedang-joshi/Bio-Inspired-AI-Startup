import math
import adafruit_sdcard
import busio
import digitalio
import microcontroller
import storage
import io
import analogio
import board

from adafruit_datetime import datetime, date

from board import *
import time
import sdcardio

def collect_data(file,LOGI):
    current_time = datetime.now()
    file.write("%0.4f\n" %(microcontroller.cpu.temperature))
    file.flush()
    time.sleep(LOGI)


spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = board.GP15
sd = sdcardio.SDCard(spi, cs)

vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

B = 4250 #Nominal B-Constant： 4250 ~ 4299K
R0 = 100000 #Zero power resistance: 100 KΩ

# Data logging time in seconds:
LOGt = 5

# Data logging interval in seconds:
LOGi = 1

# Use the filesystem as normal! Our files are under /sd
i = 0

fileappend = open("/sd/temperature.csv", "a")

while i < LOGt/LOGi:
    current_time = datetime.now()
    fileappend.write("%0.4f\n" %(microcontroller.cpu.temperature))
    fileappend.flush()
    time.sleep(LOGi)
    i += 1



