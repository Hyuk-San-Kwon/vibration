import utime
from servo import Servo
 
s1 = Servo(0)       # Servo pin is connected to GP0
 
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
# if __name__ == '__main__':
#     while True:
#         print("Turn left ...")
#         servo_Angle(30)
#         utime.sleep(1)
#         print("Turn right ...")
#         servo_Angle(180)
#         utime.sleep(1)
#         print("Turn right ...")
#         servo_Angle(0)
#         utime.sleep(1)