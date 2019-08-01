#written by Daniel Beckerich on 9/10/2017 11:20pm
#written to fulfill homework problem 2-20
#this program is designed to ask a user for an input, and it will tell the user if it is an int or not

#make the variable
user_str = ""

while True:
    #get the user input
    user_str = input("Input an integer: ")
    if(user_str.isdigit()):
        print("The integer is: " + str(user_str))
        break
    else: print("Error: Try again.")

