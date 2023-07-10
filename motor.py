import RPi.GPIO as GPIO
import time

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

speed = 45
speed2 = 82
# for i in range (5):
    # RV(speed)
    # time.sleep(5)
    # RV(0)
    # time.sleep(1)
    # R(speed)
    # time.sleep(5)
    # R(0)
    # time.sleep(1)
    # LV(speed)
    # time.sleep(5)
    # LV(0)
    # time.sleep(1)
    # L(speed)
    # time.sleep(5)
    # L(0)
    # time.sleep(1)
    
#LV takes opposite input
R(5)
time.sleep(5)
print("switch")
R(-5)
time.sleep(5)
R(0)
GPIO.cleanup()


































