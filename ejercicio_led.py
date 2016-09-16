# Ejercicio led
# fecha 16-09-2016

# Ejemplo GPIO

GPIO_RED=23
GPIO_BLUE=24
INPUT1=25

#Demora en seg
DELAY1=1

#Import RPi.GPIO module
import RPi.GPIO as GPIO

#import time module use for sleep
import time

#Use GPIO pin numbering disable in-use warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Salidas
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_BLUE, GPIO.OUT)

#Entrads
GPIO.setup(INPUT1, GPIO.IN)

cont=0
led=False

while 1:
    time.sleep (0.001)
    cont=cont+1
    if cont==1000:
        cont=0
        led=not led
        
    GPIO.output (GPIO_BLUE, led)
    
    if GPIO.input(INPUT1):
        GPIO.output (GPIO_RED, True)
    else:
        GPIO.output (GPIO_RED, False)
