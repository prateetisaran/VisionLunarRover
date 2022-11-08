import sys
from time import sleep
import pygame
import serial

pygame.init()

display = pygame.display.set_mode((300, 300))
pygame.key.set_repeat(1, 750)

arduinoSteer = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
arduinoRun = serial.Serial(port='COM4', baudrate=115200, timeout=.1) # REMEMBER TO DO THIS

throttle = 0
steering = 0





def writeSteer(x):
    global steering
    arduinoSteer.write(bytes(x, 'utf-8'))
    sleep(0.05)
    data = arduinoSteer.readline()
    steering = int(x)
    return data


def writeRun(x):
    global throttle
    arduinoRun.write(bytes(x, 'utf-8'))
    sleep(0.05)
    data = arduinoRun.readline()
    throttle = int(x)
    return data
# FIRST 0 SPEED




writeRun("58")
writeSteer("0")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            # checking if key "A" was pressed
            if event.key == pygame.K_UP:
                n_throttle = min(98, throttle + 5)
                writeRun(f"{n_throttle}")
                print(f"Throttle up to {throttle}")
            # checking if key "J" was pressed
            if event.key == pygame.K_DOWN:
                n_throttle = max(68, throttle-5)
                writeRun(f"{n_throttle}")
                print(f"Throttle down to {throttle}")

            # checking if key "P" was pressed
            if event.key == pygame.K_LEFT:
                if steering != -400:
                    n_steering = max(-400, steering -100)
                    writeSteer(f"{n_steering}")
                    print(f"Steering to {steering}")

            # checking if key "M" was pressed
            if event.key == pygame.K_RIGHT:
                if steering != 400:
                    n_steering = min(400, steering +100)
                    writeSteer(f"{n_steering}")
                    print(f"Steering to {steering}")

            if event.key == pygame.K_SPACE:
                writeRun("68")
                #writeSteer("0")

                print("Steering and throttle stopped")