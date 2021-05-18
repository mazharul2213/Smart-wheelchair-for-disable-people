#!/usr/bin/env python
import signal
import serial
import skywriter
import time
import sys
some_value = 5000
gsm=serial.Serial(’/dev/ttyS0’,baudrate=9600,timeout=5)
phone_number="017********"
#phone_number=’01*********’
sms_text="msg from gesture device"
def sendToBluetooth(msg):
try:
btDev=serial.Serial(’/dev/rfcomm0’,9600)
btDev.write(msg)
print(msg)
except:
print("bluetooth connection failed")

def send_msg():
gsm.write(’AT+CMGF=1\r\n’)
time.sleep(0.2)
print(gsm.read(gsm.inWaiting()))
sms_cmd=’AT+CMGS=\"’+phone_number+’\"\r\n’
print(sms_cmd)
gsm.write(sms_cmd)
time.sleep(1)
print(gsm.read(gsm.inWaiting()))
gsm.write(’from gesture device’+chr(26))
time.sleep(1)
print(gsm.read(gsm.inWaiting()))
@skywriter.move()
def move(x, y, z):
x+y+z
@skywriter.flick()
def flick(start,finish):
print(’Got a flick!’, start, finish)
if(start ==’west’ and finish==’east’):
sendToBluetooth(’right’)
elif(start==’east’ and finish==’west’):
sendToBluetooth(’left’)
elif(start==’south’ and finish==’north’):
sendToBluetooth(’start’)
elif(start==’north’ and finish==’south’):
sendToBluetooth(’stop’)
@skywriter.airwheel()
def spinny(delta):
global some_value
some_value += delta
if some_value < 0:

some_value = 0
if some_value > 10000:
some_value = 10000
print(’Airwheel:’, some_value/100)
@skywriter.double_tap()
def doubletap(position):
print(’Double tap!’, position)
if(position==’center’):
sendToBluetooth(’stop’)
@skywriter.tap()
def tap(position):
print(’Tap!’, position)
send_msg()
time.sleep(1)
@skywriter.touch()
def touch(position):
print(’Touch!’, position)
signal.pause()

