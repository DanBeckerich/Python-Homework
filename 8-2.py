#Written by Daniel Beckerich
#on 12/2/2017
#for exercise 17 of chapter 8

from sys import stdout

#test data
nums = [1,2,3,4,5,6];

#get even numbers
#itterate through a given list of numbers, returning the even numbers. 
def remove_odd_nums(in_list):
	out_list = [];
	for i in range(len(in_list)):
		if (in_list[i] % 2) == 0:
			out_list.append(in_list[i])
	return out_list

#get the odd numbers
#itterate through a given list of numbers, returning the odd numbers. 
def remove_even_nums(in_list):
	out_list = [];
	for i in range(len(in_list)):
		if (in_list[i] % 2) != 0:
			out_list.append(in_list[i])
	return out_list

#selectable version.
def get_num(in_list,in_bool):
	if (in_bool):
		return(remove_odd_nums(in_list))
	else:
		return(remove_even_nums(in_list))

#print the data in a nice format.
stdout.write("Test Data: ")
stdout.write(str(nums))
stdout.write("\n")

stdout.write("Even numbers: ")
stdout.write(str(get_num(nums,True)))
stdout.write("\n")

stdout.write("Odd numbers: ")
stdout.write(str(get_num(nums,False)))
stdout.write("\n")
