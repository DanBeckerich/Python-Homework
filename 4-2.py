#Written by Daniel Beckerich
#on 10/19/2017

#set the exit flag to false
should_exit = False

while should_exit == False:
    #get the user input and convert it to an int
    user_input_raw = input("Enter a 3-digit number in asccending order: ")
    user_input = int(user_input_raw)

    if user_input in range(100,999):
        #get the ones, tens, and hundred place
        Hundreds_place = int(user_input_raw[0])
        Tens_place = int(user_input_raw[1])
        Ones_place = int(user_input_raw[2])

        if(Hundreds_place < Tens_place < Ones_place):
            print("that is an acceptable number")
            should_exit = True

