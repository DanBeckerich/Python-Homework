#written by Daniel beckerich on 10/12/2017
#this program is designed to fulfill the requirements for exercise 48 in chapter 4

#import the sys package so we can contol the consol better
import sys

#itterate
for x in range(13):
    for y in range(13):
        if x*y in range(10):
            sys.stdout.write(str(x*y) + "   ")
        elif x*y in range(10,100):
            sys.stdout.write(str(x*y) + "  ")
        elif x*y in range(100,1000):
            sys.stdout.write(str(x*y) + " ")
        else:
            sys.stdout.write(str(x*y) + " ")
    sys.stdout.write("\n")
