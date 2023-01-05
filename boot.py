#Boot.py for ESP32


import sys

sys.path.append("")

from micropython import const

import uasyncio as asyncio
import aioble
import bluetooth

import random
import struct

import time
from time import sleep
from machine import I2C, Pin
import ssd1306
from time import sleep, localtime
from machine import RTC
from machine import Timer
import utime
import ntptime
import machine

from machine import Pin

async def find_temp_sensor():
    # Scan for 5 seconds, in active mode, with very low interval/window (to
    # maximise detection rate).
    async with aioble.scan(5000, interval_us=30000, window_us=30000, active=True) as scanner:
        async for result in scanner:
            # See if it matches our name and the environmental sensing service.
            if result.name()=="CIRCUITPY5acc":
                return (result.device)
    return None


async def main():
    pin =Pin(27, Pin.OUT)
    device = await find_temp_sensor()
    if not device:
        device = await find_temp_sensor()
        return

    try:
        print("Connecting to", device)
        connection = await device.connect()
    except asyncio.TimeoutError:
        print("Timeout during connection")
        return

    async with connection:
        try:
            pin.on()
        except asyncio.TimeoutError:
            print("Timeout discovering services/characteristics")
            return

asyncio.run(main())



i2c = I2C(-1, scl=Pin(22), sda=Pin(23))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
btnA = Pin(26, Pin.IN)
btnB = Pin(25, Pin.IN)
btnC = Pin(34, Pin.IN)
btnD = Pin(39, Pin.IN)

monster_A = [
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 1, 1, 1, 1, 0, 1],
    [ 0, 1, 0, 1, 1, 0, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 0, 0],
    [ 1, 1, 0, 1, 1, 0, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 0, 1],
]

monster_B = [
    [ 0, 1, 0, 0, 0, 0, 1, 0],
    [ 0, 1, 1, 0, 0, 1, 1, 0],
    [ 0, 0, 1, 0, 0, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 0, 0, 0],
    [ 0, 0, 1, 1, 1, 1, 0, 0],
    [ 0, 1, 0, 1, 1, 0, 1, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 0, 0, 1, 1, 0],
]


i=1
flag = 1 # to swap the monster
ICON = monster_A # initially defining monster As

# This function switches the monsters
def Change_Monster():
    global ICON
    global flag
    # Swapping monster while button pressed
    if(flag==1):
        ICON = monster_B
        flag = 0
    else :
        ICON = monster_A
        flag = 1
    # Calling draw function    
    Draw()

# This function draws the monster       
def Draw():
    global i
    oled.fill(0)
    # Showing monster in the oled screen
    for y, row in enumerate(ICON):
        for x, c in enumerate(row):
            oled.pixel(x+i, y, c)
    oled.show()

# Moves the monster
def Shift(val):
    global i
    if(val==1):
       i=int(i)+1
       if i==121:
        i=1
       
    else :
        i=int(i)-1 
        if i == 0:
            i = 120
    
    Draw()    
    
    
# Get connection with the network    
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Nushrat', 'idontcare')
        while not wlan.isconnected():
            pass
    print('Connection alive')
    t = ntptime.time()
    tm = utime.gmtime(t+3600)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
    time.gmtime()

# Shows date and time   
def fun():
    var = localtime()
    date = str(var[0]) + "-" + str(var[1]) +"-" + str(var[2])
    time = str(var[3]) + ":" + str(var[4]) +":" + str(var[5])

    oled.fill(0)
    oled.show()
    do_connect()
    oled.text(date, 0, 0, 1)
    oled.text(time, 0, 8, 1)
    oled.show()

# Calls fun() periodically
def Take_Time():
    tim0 = Timer(0)
    tim0.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:fun())
    
 
    
def Btn_IRQ():
    P26 = Pin(26, Pin.IN)
    P25 = Pin(25, Pin.IN)
    P34 = Pin(34, Pin.IN)
    P39 = Pin(39, Pin.IN)
    
    P26.irq(lambda p: Shift(1))
    P25.irq(lambda p: Shift(2))
    P34.irq(lambda p: Change_Monster())
    P39.irq(lambda p: Take_Time())
    
Btn_IRQ()