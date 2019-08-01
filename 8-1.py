#Written by Daniel Beckerich
#on 12/2/2017
#for exercise 10 of chapter 8
#This program is designed return the smallest and largest number from a list of numbers.

#im using this library so i get full control over the consol.
from sys import stdout

test_list = [1,2,3,4,5,0];

def smallest_and_largest(list1):
	smallest= 0
	largest= 0
	#if the current number is smaller than the smallest, save it in smallest. if its larger than largest, save it in largest.

	for i in range(len(list1)):
		if list1[i] > largest:
			largest = list1[i]
		elif list1[i] < largest:
			smallest = list1[i]
	if smallest == largest:
		return (smallest,)
	#if the numers are the same, only return one item in the tuple.
	else:
		return (smallest, largest)

temp = smallest_and_largest(test_list)
for i in range(len(temp)):
	stdout.write(str(temp[i]) +" ")