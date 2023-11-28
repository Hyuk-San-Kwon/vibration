# import time
# from machine import Pin, PWM

from machine import Pin, PWM
import time
# import utime

def set_motor_speed(v, motor1b, motor2b ,pwm_1, pwm_2):
    
    motor1b.low()
    pwm_1.duty_u16(v)
    time.sleep(2)
    
    motor2b.low()
    pwm_2.duty_u16(v)
    time.sleep(2)