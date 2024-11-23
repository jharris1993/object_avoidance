# Base version of Object Avoidance Robot as created in advanced Bloxter

import easygopigo3 as easy
import time
import random
import os
import sys


gpg = easy.EasyGoPiGo3()
my_distance_portI2C = gpg.init_distance_sensor('I2C')
time.sleep(0.1)

print("sys.path", sys.path)
print("pythonpath", PYTHONPATH)
exit()
# start
while True:
    while my_distance_portI2C.read_inches() > 12:
        gpg.forward()
    time.sleep (2)
    gpg.backward()
    time.sleep(4)
    gpg.stop()
    gpg.turn_degrees((random.randint(90, 270)), blocking=True)
    time.sleep(0.05) # slowdown
