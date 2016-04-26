
# My Thor solution on CodinGame

import sys
import math

# X=39=absolute_EAST
# X=0=absolute_WEST
# Y=17=absolute_SOUTH
# Y=0=absolute_NORTH


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

# let's rename the initial vars, and use them to track Thor's movement
x, y = initial_tx, initial_ty

# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

	# if the light is diagonally below...
	if y < light_y and x > light_x:
		x, y = x - 1, y + 1 
		print "SW"
	elif y < light_y and x < light_x:
		x, y = x + 1, y + 1
		print "SE"
	
	# if the light is diagonally above...
	elif y > light_y and x < light_x:
		x, y = x - 1, y - 1
		print "NW"
	elif y > light_y and x > light_x:
		x, y = x + 1, y - 1
		print "NE"
	
	# if the light is west or east...
	elif x > light_x:
		x = x - 1
		print "W"
	elif x < light_x:
		x = x + 1
		print "E"
		
	# if the light is north or south...
	elif y > light_y:
		y = y - 1
		print "N"
	elif y < light_y:
		y = y + 1
		print "S"


