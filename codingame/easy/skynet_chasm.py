import sys
import math


road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.

# game loop
while True:
    speed = int(raw_input())  # the motorbike's speed.
    coord_x = int(raw_input())  # the position on the road of the motorbike.

    # bike needs to go faster than space of gap
    if speed < gap + 1 and coord_x < road:
        print "SPEED"

    # but not faster than needed, or should slow if past gap
    elif speed > gap + 1 or coord_x >= road + gap:
        print "SLOW"
    
    # if bike is just before the gap,
    elif road - speed < coord_x < road:
        print "JUMP"
    
    else:
        print "WAIT"

