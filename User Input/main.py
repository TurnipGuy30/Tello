# import dependencies
from djitellopy import Tello
import cv2
import time

# create input variable
a = ''

# documentation
t = Tello()
i = time

# intro and controls
input('''
DRONE CONTROL

Hello! Welcome to the Tello Drone control panel!

I would recommend using splitscreen to have this
window on the left and the control table on the
right.

INSTRUCTIONS

When you see 'In', press the key associated with
the command you want to run, and press Enter.
Wait until you see 'In' again, and repeat. All
key codes are lowercase.

IMPORTANT KEYS

- Takeoff and Land are K and M
- Moving is WASD, and type two (e.g. 'ww') to go
further ('w' = 50cm, 'ww' = 1m)
- Emergency Land is ']'
- To end the program, press '['

When you're ready to go, press Enter to continue.
''')

# connect to drone
t.connect()
i.sleep(1)

# input loop, '[' to end
while a != '[':

    a = input('In: ').lower()

    if a == 'q':
        t.streamon()

    elif a == 'w':
        t.move_forward(50)

    elif a == 'ww':
        t.move_forward(100)

    elif a == 'e':
        t.streamoff()

    elif a == 'r':
        t.get_frame_read()
        t.get_video_capture()

    elif a == 't':
        t.flip_forward()

    elif a == 'y':
        t.get_temperature()

    elif a == 'u':
        t.get_distance_tof()

    elif a == 'i':
        t.get_speed()

    elif a == 'o':
        t.rotate_counter_clockwise(45)

    elif a == 'p':
        t.rotate_clockwise(45)

    # elif a == '[':
        # exit loop

    elif a == ']':
        t.emergency()

    elif a == 'a':
        t.move_left(50)

    elif a == 'aa':
        t.move_left(100)

    elif a == 's':
        t.move_back(50)

    elif a == 'ss':
        t.move_back(100)

    elif a == 'd':
        t.move_right(50)

    elif a == 'dd':
        t.move_right(100)

    elif a == 'f':
        t.flip_left()

    elif a == 'g':
        t.flip_back()

    elif a == 'h':
        t.flip_right()

    elif a == 'j':
        t.get_flight_time()

    elif a == 'k':
        t.takeoff()

    elif a == 'l':
        t.rotate_counter_clockwise(90)

    elif a == ';':
        t.rotate_clockwise(90)

    elif a == '\'':
        t.move_up()

    elif a == 'z':
        t.move_up(50)

    elif a == 'zz':
        t.move_up(100)

    elif a == 'x':
       t.move_down(50)

    elif a == 'xx':
        t.move_down(100)

    elif a == 'c':
        t.get_attitude()

    elif a == 'v':
        t.get_barometer()

    elif a == 'b':
        t.get_battery()

    elif a == 'n':
        t.get_height()

    elif a == 'm':
        t.land()

    elif a == ',':
        t.get_wifi()

    elif a == '.':
        t.connect()

    elif a == '/':
        t.end()

    print('')
    i.sleep(0.05)

# end if '[' is entered
t.land()
t.end()

# finish
print('')
input('Thank you for using my Drone Control!')
