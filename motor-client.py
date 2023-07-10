import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

DirRV=17 # GPIO 17 is pin 11
PwmRV=27 # GPIO 27 is pin 13
GPIO.setup(PwmRV,GPIO.OUT)
GPIO.setup(DirRV,GPIO.OUT)
rv=GPIO.PWM(PwmRV,100)

DirR=2 # pin 3
PwmR=10 # pin 19
GPIO.setup(DirR,GPIO.OUT)
GPIO.setup(PwmR,GPIO.OUT)
r=GPIO.PWM(PwmR,100)

DirL=9 # 21
PwmL=11 # 23
GPIO.setup(DirL,GPIO.OUT)
GPIO.setup(PwmL,GPIO.OUT)
l=GPIO.PWM(PwmL,100)

DirLV=5 # 29
PwmLV=6 # 31
GPIO.setup(DirLV,GPIO.OUT)
GPIO.setup(PwmLV,GPIO.OUT)
lv=GPIO.PWM(PwmLV,100)

def L(z):
	if(z<=0):
		GPIO.output(DirL,GPIO.HIGH)
	else:
		GPIO.output(DirL,GPIO.LOW)
	l.start(abs(z))

def LV(z):
	if(z<=0):
		GPIO.output(DirLV,GPIO.HIGH)
	else:
		GPIO.output(DirLV,GPIO.LOW)
	lv.start(abs(z))
		
def R(z):
	if(z<=0):
		GPIO.output(DirR,GPIO.HIGH)
	else:
		GPIO.output(DirR,GPIO.LOW)
	r.start(abs(z))

def RV(z):
	if(z<=0):
		GPIO.output(DirRV,GPIO.HIGH)
	else:
		GPIO.output(DirRV,GPIO.LOW)
	rv.start(abs(z))
	
# 60 messages/second
timestep = 1.0/60.0
running = True
while (running):
    response = requests.get("http://10.42.0.1:5000/controller")
    response = response.json()
    print(response)
    x, y, xySpd = 0, 0, 0
    if (abs(response[0]) >= 0.5):
        x = response[0]
    if (abs(response[1]) >= 0.5):
        y = response[1]
    if (response[3] >= 0.2): xySpd = -response[3]
    #forwarding overrides reverse trigger
    if (response[2] >= 0.2): xySpd = response[2]
    xySpd *= 100
    print(xySpd, x, y)
    #L is R and R is L
    if (abs(x) > 0.25): #we turning
    	if (x >= 0):
    	    LV(xySpd)
    	    RV(-xySpd)
    	else:
    	    LV(-xySpd)
    	    RV(xySpd)
    else: #go straight forward or backwards
    	LV(xySpd)
    	RV(xySpd)
    	
    #height controls
    if (response[4] == 1):# A pressed so we want to go up
    	R(100)
    	L(100)
    elif (response[5] == 1): # B pressed (overriden by A) so we want to go down
    	R(-100)
    	L(-100)
    else:#else neutral
    	R(0)
    	L(0)




























