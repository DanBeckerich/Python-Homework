#9/10/2017 11:50pm
#written by Daniel Beckerich for homework problem 2-38
#this program is designed to sum all digits in a number. i.e. 28 = 10 or 2 + 8 = 10

#create the variables
user_str = ""
result = 0

#get the user data and validate that it is a number by using the code from the last HW problem
while True:
    #get the user input
    user_str = input("Input an integer: ")
    if(user_str.isdigit()):
        break
    else: print("Error: Try again.")
#convert the string to a list
result = sum(map(int,user_str))
#print out the sum
print("the sum of all digits is: " + str(result))

