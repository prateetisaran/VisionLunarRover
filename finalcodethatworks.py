from time import sleep
import pygame
import serial


# SETUP OF ARDUINO AND CONTROLLER
pygame.init()
pygame.joystick.init()
c = pygame.joystick.Joystick(0)
c.init()

axis_data = {}

arduinoSteer = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
arduinoRun = serial.Serial(port='COM4', baudrate=115200, timeout=.1) # REMEMBER TO DO THIS


# HYPERPARAMETERS
z=1.25 #set to min (this is the delay time)



# READING AND WRITING FUNCTIONS
def read_controller_input(axis_data):
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axis_data[event.axis] = round(event.value, 4)
    try:
        steering = int(axis_data[0] * 400.0)  # Input values are between -1.0 and 1.0
    except KeyError:
        steering = 0

    try:
        if float(axis_data[5]) == 0.0:
            throttle = 63
        else:
            throttle = 63 + int((axis_data[5] + 1.0) * (10.0))  # Input values are between -1.0 and 1.0, final values are between 60 and 200
    except KeyError:
        throttle = 63

    return steering, throttle, axis_data

def writeSteer(x):
    global steer
    arduinoSteer.write(bytes(x, 'utf-8'))
    sleep(0.1)
    data = arduinoSteer.readline()
    steer = x
    return data


def writeRun(x):
    global speed
    arduinoRun.write(bytes(x, 'utf-8'))
    sleep(0.05)
    data = arduinoRun.readline()
    speed = x
    return data
# FIRST 0 SPEED
# write code to set speed to 0
speed = 0
steer = 0


print("starting")
# MAIN LOOP
while True:
    steering, throttle, axis_data = read_controller_input(axis_data) # Steering [-400,400] and Throttle [0,100]
    writeSteer(f"{steering}")
    writeRun(f"{throttle}")

    print(f"""Current speed = {speed}
Current steering = {steer}""")

    sleep(0.75)
