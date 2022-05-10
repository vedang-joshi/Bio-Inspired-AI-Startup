import board
import digitalio
import simpleio
import time
import pwmio
import audiocore
import audiopwmio
import array
import time
import math
import adafruit_sdcard
import busio
import microcontroller
import storage
import io
import analogio

from adafruit_datetime import datetime, date

from board import *
import sdcardio

# Global variables
button1_pressed = False
button2_pressed = False
button3_pressed = False
button_pressed_flag = True

def waiting_for_button(duration):
    global button1_pressed
    global button2_pressed
    global button3_pressed
    end = time.monotonic() + duration
    while time.monotonic() < end:
        if button1.value == False:
            button1_pressed = True
        if button2.value == False:
            button2_pressed = True
        if button3.value ==  False:
            button3_pressed = True

def button1_handler():
    
    #Deinitialize button pins
    global button1
    global button2
    global button3
    button1.deinit()
    button2.deinit()
    button3.deinit()
    
    global button_pressed_flag
    global button1_pressed
    spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
    cs = board.GP15
    sd = sdcardio.SDCard(spi, cs)

    vfs = storage.VfsFat(sd)
    storage.mount(vfs, '/sd')

    B = 4250 #Nominal B-Constant： 4250 ~ 4299K
    R0 = 100000 #Zero power resistance: 100 KΩ

    # Data logging time in seconds:
    LOGt = 90
    
    # Data logging interval in seconds:
    LOGi = 0.2
    
    # Use the filesystem as normal! Our files are under /sd
    i = 0
    
    fileappend = open("/sd/temperature_fridge.csv", "a")
    fileappend.write("new_data_collection\n")
    #potentiometer = analogio.AnalogIn(board.GP27)
    
    while i < LOGt/LOGi:
        collect_data(file=fileappend, LOGI=LOGi)
        i += 1
        
        #button_pressed_flag = False
        #if not button_pressed_flag:
        #    button_pressed_flag = True
        #    break
    storage.umount(vfs)
    sd.deinit()
    spi.deinit()
    #Initialize button pins
    button1 = digitalio.DigitalInOut(board.GP20)
    button1.switch_to_input(pull=digitalio.Pull.UP)
    button2 = digitalio.DigitalInOut(board.GP21)
    button2.switch_to_input(pull=digitalio.Pull.UP)
    button3 = digitalio.DigitalInOut(board.GP22)
    button3.switch_to_input(pull=digitalio.Pull.UP)
    time.sleep(0.5)

def collect_data(file,LOGI):
    # append to the file!
    #tempval = sensor.value
    #print(tempval)
    #R = (1023/tempval)-1;
    #R = R0*R;

    #temperature = (1/(math.log(abs(R/R0))/B+1/298.15)-273.15)-1.5
    #print(temperature)
    current_time = datetime.now()
    file.write("%0.4f\n" %(microcontroller.cpu.temperature))
    file.flush()
    time.sleep(LOGI)


def startup():
    # Melody
    POWERUP_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
    POWERUP_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

    # Define pin connected to piezo buzzer
    PIEZO_PIN = board.GP22
    
    # Generate one period of sine wav.
    length = 8000 // 440
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15) + 2 ** 15)

    dac = audiopwmio.PWMAudioOut(board.GP18)
    sine_wave = audiocore.RawSample(sine_wave, sample_rate=8000)
    dac.play(sine_wave, loop=True)
    time.sleep(1)
    dac.stop()
    
    #Initialize button pins
    global button1
    global button2
    global button3
    button1 = digitalio.DigitalInOut(board.GP20)
    button1.switch_to_input(pull=digitalio.Pull.UP)
    button2 = digitalio.DigitalInOut(board.GP21)
    button2.switch_to_input(pull=digitalio.Pull.UP)
    button3 = digitalio.DigitalInOut(board.GP22)
    button3.switch_to_input(pull=digitalio.Pull.UP)
    
    '''
    while True:
        # Check button 1 (GP20)
        if not button1.value:
            spi = busio.SPI(GP10, MOSI=GP11, MISO=GP12)
            cs = GP15
            sd = sdcardio.SDCard(spi, cs)
             
            vfs = storage.VfsFat(sd)
            storage.mount(vfs, '/sd')

            B = 4250 #Nominal B-Constant： 4250 ~ 4299K
            R0 = 100000 #Zero power resistance: 100 KΩ


            # Data logging time in seconds:
            LOGt = 10

            # Data logging interval in seconds:
            LOGi = 1

            # Use the filesystem as normal! Our files are under /sd
            i = 0
    
            fileappend = open("/sd/temperature.csv", "a")
            potentiometer = analogio.AnalogIn(board.GP27)
            # append to the file!
            while True:
                tempval = potentiometer.value
                #print(tempval)
                R = (1023/tempval)-1;
                R = R0*R;
        
                temperature = (1/(math.log(abs(R/R0))/B+1/298.15)-273.15)-1.5
                #print(temperature)
                current_time = datetime.now()
                fileappend.write("%s,%0.4f\n" %(str(current_time),temperature))
                fileappend.flush()
                time.sleep(LOGi)
                i += 1
                
        # Check button 2 (GP21)
        elif not button2.value:
            break  

        time.sleep(0.1) # sleep for debounce
        '''
startup()

while True:
    waiting_for_button(1)

    if button1_pressed:
        button1_handler()
        waiting_for_button(0.2)
        button1_pressed = False
    elif button3_pressed:
        break

