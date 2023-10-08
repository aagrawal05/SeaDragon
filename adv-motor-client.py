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
	
# 120 messages/second
timestep = 1.0/120.0
running = True
inplace_turn, switched = False, False
coyote_time = 10
cur_time = 0
spd_dead_zone = 0.2
x_dead_zone = 0.5
while (running):
    response = requests.get("http://10.42.0.1:5000/controller")
    response = response.json()
    print(response)
    x, xySpd = 0, 0
    if (abs(response[0]) >= x_dead_zone):
        x = response[0]
    if (response[3] >= spd_dead_zone): xySpd = -response[3]
    #forwarding overrides reverse trigger
    if (response[2] >= spd_dead_zone): xySpd = response[2]
    xySpd *= 100
    print(xySpd, x)
    if (switched): cur_time += 1
    if (cur_time >= coyote_time): switched = False
    if (response[9] == 1 and not switched): 
        inplace_turn = not inplace_turn
        switched = True
        cur_time = 0
    
    print(inplace_turn)
    lvSpd = xySpd
    rvSpd = xySpd
    lSpd, rSpd = 0, 0
    if (abs(x) > 0.25): #we turning
    	if (x >= 0):
    	    rvSpd = -xySpd if inplace_turn else 0
    	else:
    	    lvSpd = -xySpd if inplace_turn else 0
    	
    #height controls
    if (response[4] == 1):# A pressed so we want to go up
        rSpd, lSpd = 100, 100
    elif (response[5] == 1): # B pressed (overriden by A) so we want to go down
        rSpd, lSpd = -100, -100
    	
    #Override A, B button presses using bumpers
    #Get control over a specific side to push up
    if (response[6] == 1): #Left Bumper so push up front right
    	rSpd = 100
    if (response[7] == 1): #Right Bumper so push up front left
        lSpd = 100
    
    L(lSpd)
    R(rSpd)
    LV(lvSpd)
    RV(rvSpd)

GPIO.cleanup()
