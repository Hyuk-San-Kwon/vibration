from machine import Pin, PWM
import utime

# fast

en1 = Pin(4, Pin.OUT)
# en2 = Pin(7, Pin.OUT)
 
en1(1)  # motor 1 enable, set value 0 to disable
motor1a = Pin(2, Pin.OUT)
motor1b = Pin(3, Pin.OUT)


def forward():
    motor1a.high()
    motor1b.low()
    
def backward():

    motor1a.low()
    motor1b.high()
    
def stop():

    motor1a.low()
    motor1b.low()

def testMotor():
    forward()
    utime.sleep(5)
    stop()
    utime.sleep(1)
    # backward()
    # utime.sleep(2)
    # stop()
    # utime.sleep(2)

print("OK...")
print("RPi-PICO with DC Motor")

while True:
        
    testMotor()
        