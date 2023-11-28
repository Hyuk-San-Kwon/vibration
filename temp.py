import time
# from machine import Pin, PWM

from machine import Pin, PWM
# import utime

# fast

# def set_motor_speed(m, pwm, v):
#     m.low()
#     pwm.duty_u16(v)
    

m3 = Pin(3, Pin.OUT)
m2 = Pin(2, Pin.OUT)

en1 = Pin(4, Pin.OUT)
en1(1) 


pwm_b = PWM(Pin(2))
pwm_b.freq(20000)

m3.low()
pwm_b.duty_u16(65535)
time.sleep(2)


m3.low()
pwm_b.duty_u16(16383)
time.sleep(2)


m3.low()
pwm_b.duty_u16(0)
