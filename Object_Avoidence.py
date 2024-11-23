# Object Avoidance Robot

import easygopigo3 as easy
import time
import random

gpg = easy.EasyGoPiGo3()
gpg = easy.EasyGoPiGo3()
servo_1 = gpg.init_servo('SERVO1')
servo_2 = gpg.init_servo('SERVO2')
sleep_time = 0.50  # pause time in seconds

my_distance_portI2C = gpg.init_distance_sensor('I2C')
time.sleep(0.1)

print("Running: Test Servos.\n")

# Read the connected robot's serial number
serial_number = gpg.get_id() # read and display the serial number

# For testing only - "invalid" serial number
# serial_number = "invalid"

print("This robot's serial number is\n"+serial_number+"\n")


# Servo constants for each robot

# Each robot is identified by its unique serial number

# Charlene:
if serial_number == "A0F6E45F4E514B4B41202020FF152B11":

# Charlene's servo constants
    print("Robot is \"Charlene\"")
    center_1 = 86  # Horizontal centering - smaller is further right.
    center_2 = 76  # Vertical centering - smaller is further up.

# Charlie:
elif serial_number == "64B61037514E343732202020FF111A05":

# Charlie's servo constants
    print("Robot is \"Charlie\"")
    center_1 = 86  # Horizontal centering - smaller is further right.
    center_2 = 90  # Vertical centering - smaller is further up.

else:
# Unknown serial number
    print("I don't know who robot", serial_number, "is,")
    print("If we got this far, it's obviously a GoPiGo robot")
    print("But I don't know what robot it is, so I'm using")
    print("the default centering constants of 90/90.\n")

# Default servo constants
    print("Robot is \"Unknown\"")
    print("Please record the robot's serial number, name,")
    print("and derived centering constants.")
    center_1 = 90
    center_2 = 90

# Start Test Servos

# Define excursions
right = center_1 - 45
left = center_1 + 45
up = center_2 - 45
down = center_2 + 45

def test_servos():
    # Test servos
    print("\nStarting test:")
    print("Using centering constants "+str(center_1)+"/"+str(center_2), "for this robot")

    print("\nCenter Both Servos")
    servo_1.rotate_servo(center_1)
    servo_2.rotate_servo(center_2)
    time.sleep(sleep_time)

    print("Test Servo 1 (horizontal motion)")
    servo_1.rotate_servo(right)
    time.sleep(sleep_time)
    servo_1.rotate_servo(left)
    time.sleep(sleep_time)
    servo_1.rotate_servo(center_1)
    time.sleep(sleep_time)

    print("Test Servo 2 (vertical motion)")
    servo_2.rotate_servo(up)
    time.sleep(sleep_time)
    servo_2.rotate_servo(down)
    time.sleep(sleep_time)

    print("Re-Center Both Servos")
    servo_1.rotate_servo(center_1)
    servo_2.rotate_servo(center_2)
    time.sleep(sleep_time)
    servo_1.disable_servo()
    servo_2.disable_servo()
    print("Complete: Test Servos - Exiting.")

def avoid():
    while True:
        while my_distance_portI2C.read_inches() > 20:
            gpg.forward()
        gpg.stop()
        time.sleep(1)
        gpg.backward()
        time.sleep(1)
        gpg.stop()
        test_servos()
        gpg.backward()
        time.sleep(4)
        gpg.stop()
        time.sleep(1)
        gpg.turn_degrees((random.randint(90, 270)), blocking=True)
        time.sleep(1) # slowdown


#------------------------------------
# Main routine entry point is here
#------------------------------------

if __name__ == "__main__":
    test_servos()  # make sure servos are centered
    avoid()
    logging.info("Finished!")
    sys.exit(0)
