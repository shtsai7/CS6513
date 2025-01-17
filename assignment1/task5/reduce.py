#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy


'''
    Try parse input string to integer.
'''
def tryParseInt(input):
    try:
        intValue = int(input)
        return True, intValue
    except ValueError:
        return False, -1


currentKey = None
currentCount = 0
maxKey = None
maxCount = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')
    success, intValue = tryParseInt(value)

    if not success:
        continue

    if key == currentKey:
        currentCount += intValue

    else:
        if currentKey:
            if currentCount > maxCount:
                maxKey = currentKey
                maxCount = currentCount

        currentKey = key
        currentCount = intValue


# Compute/output result for the last key
if currentKey:
    if currentCount > maxCount:
        maxKey = currentKey
        maxCount = currentCount

print('{0:s}\t{1:d}'.format(maxKey, maxCount))


