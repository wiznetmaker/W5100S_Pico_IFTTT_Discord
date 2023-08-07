from usocket import socket
from machine import Pin,SPI
import network
import time
import urequests

button_pin1 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin2 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin3 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin4 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin5 = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    nic.ifconfig(('192.168.0.20','255.255.255.0','192.168.0.1','8.8.8.8'))
    while not nic.isconnected():
        time.sleep(1)
    #print(nic.regs())
    #print(nic.ifconfig())

def main():
    w5x00_init()
    x=0
    while True:
        if button_pin1.value() == 0:
            print("Button1 is pressed!")
            message ="Looks%20like%20it's%20gonna%20be%20an%20overtime%20night...%20Sorry,%20no%20gaming%20for%20me%20today."
            x = 1
        if button_pin2.value() == 0:
            print("Button2 is pressed!")
            message = "Got%20some%20work%20stuff%20to%20handle,%20so%20I%20might%20be%20running%20a%20bit%20late.%20Go%20ahead%20and%20start%20without%20me."
            x = 1
        if button_pin3.value() == 0:
            print("Button3 is pressed!")
            message = "Just%20a%20teeny-tiny%20bit%20late%20for%20home%20run!%20Hold%20off%20on%20the%20kick-off,%20won't%20ya?"
            x = 1
        if button_pin4.value() == 0:
            print("Button4 is pressed!")
            message = "Let's%20dive%20right%20into%20the%20game!%20Hurry%20on%20over!"
            x = 1
        if button_pin5.value() == 0:
            print("Button5 is pressed!")
            message = "Today's%20the%20day%20we%20hit%20platinum.%20Let's%20pull%20an%20all-nighter!%20Follow%20my%20lead!"
            x = 1
            
        if x == 1:
            send_data = "https://maker.ifttt.com/trigger/applets_name/with/key/Your_key?value1={}".format(message)
            urequests.post(send_data)
            print("Complete!")
            x = 0
                
if __name__ == "__main__":
    main()



