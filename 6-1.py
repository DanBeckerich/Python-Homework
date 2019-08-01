#Written by Daniel Beckerich
#on 11/2/2017
#this program is for chapter 6 exercise 10
#this program is designed to do a short calculation, with error handling.

#Start the try statement
try:
    num4 = 0

    #get all the needed data
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    num3 = int(input("enter the third number: "))

    #do the math and print it out
    num4 = (num1/num2) + num3
    print("(" + str(num1) + "/" + str(num2) + ")" + "+" + str(num3) + "=" + str(num4))

#catch the two errors we are looking for.
except ValueError:
        print("that is not a valid number")
except ZeroDivisionError:
        print("do not devide by zero")

