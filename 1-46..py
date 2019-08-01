#this program is written by Daniel Beckerich
#on 9/10/2017 10:58pm
#this program is supposed to fulfill the instructions on p.83 for problem 46
#the purpose is to calculate how long a runner would take to run set distances given a constant rate of speed

#first, prompt the user to enter the speed of the runner
user_str = input("please enter the runners speed in mph: ")
user_flt = float(user_str)

print("Time to run 5 miles: " + str(5/user_flt) + " hours")
print("time to run 10 miles: " + str(10/user_flt) + " hours")
print("time to run a half marathon: " + str(13.1/user_flt) + " hours")
print("Tome to run a marathon: " + str(26.2/user_flt) + " hours")
