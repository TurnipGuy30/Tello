# import dependencies
from djitellopy import *
import cv2
import time

# documentation
t = Tello()
ti = time

# user assurance
print('')
print('Performing task...')

# define function
def triangle():
    for ti in range(3):
        t.move_forward(100)
        ti.sleep(1)
        t.rotate_clockwise(135)
        ti.sleep(1)

# connect to drone
t.connect()
t.takeoff()

# call function
triangle()

# move up
t.move_up(100)
ti.sleep(1)

# call function
triangle()

# end drone connection
t.land()
t.end()

# show done
print('')
input('Done! Press Enter to exit.')
