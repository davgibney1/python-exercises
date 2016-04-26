# ideas..
# sort the list
# make a new list with all the ints coverted to absolute value
# find the closest int from that new list, and if there is no mode, you're done.
# if there is a mode of that int, go back to the sorted list


###
# loick's solution:
# i=raw_input
# i()
# print -(sorted((abs(a),-a)for a in map(int,i().split()))+[(0,0)])[0][1]
###


import sys
import math
import re

# Important note: the temps var is a string, and not a list of integers!
# Also: my code sucks! This is not efficient code AT ALL. Nor is it succinct! Blah! :(
# For code to do this on larger data sets, you would need to look into bisection algorithms

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526

## Need to convert temps var from string to list of ints
# Regex to find the ints and put them in a list
temps = re.findall("[-+]?\d+[\.]?\d*", temps)
# ..but it's still a list of strings, so let's type cast to int
temps = [int(i) for i in temps]

# if there are no temps
if len(temps) < 1:
    print "0"
    
# Is there only one number in the list?
if len(temps) == 1:
    print temps[0]
    
# Is there a zero in the list?
for num in temps:
    if num == 0:
        print "0"
        # We are already done!



# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
# print >> sys.stderr, temps


########################################
#### FIND LOWEST POSITIVE NUMBER #######

# Make list out of only the positive numbers
pos_temps = []
for num in temps:
    if num > 0:
        pos_temps.append(num)

# Find lowest positive
lowest = None

# Do an initial comparison
if len(pos_temps) > 1: 
    wehavepos = True
    if pos_temps[0] < pos_temps[1]:
        lowest = pos_temps[0]
    else:
        lowest = pos_temps[1]
    # Knowing the first comparison, we can find our target
    for num in pos_temps:
        if num < lowest:
            lowest = num
else:
    wehavepos = False


########################################
#### FIND GREATEST NEGATIVE NUMBER #####

# Make list out of only the negative numbers
neg_temps = []
for num in temps:
    if num < 0:
        neg_temps.append(num)

greatest = None

# Do an initial comparison
if len(neg_temps) > 1:
    wehaveneg = True
    if neg_temps[0] > neg_temps[1]:
        greatest = neg_temps[0]
    else:
        greatest = neg_temps[1]
    # Knowing the first comparison, we can find our target
    for num in neg_temps:
        if num > greatest:
            greatest = num
else:
    wehaveneg = False
        


########################################
#### COMPUTE FINAL RESULT ############## 

# just curious, what ints we get in the test cases..
print >> sys.stderr, temps

if wehavepos and wehaveneg:
    if abs(greatest) == abs(lowest):
        print lowest
    elif abs(greatest) - abs(lowest) > 0:
        print lowest
    else:
        print greatest
elif wehavepos:
    print lowest
elif wehaveneg:
    print greatest

