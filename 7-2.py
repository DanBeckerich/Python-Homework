#Written by Daniel Beckerich
#on 12/2/2017
#for exercise 53 of chapter 7
#this program is designed to allow the user to do math with fractions, with the numbers stored in tuples.

#im using this library so i get full control over the consol.
from sys import stdout

tup1 = (1,2);
tup2 = (3,4);

def add_fraction(tup1,tup2):
	#variables for both the numerator and denominator. these will be paired in a tuple for output later.
	result_num = 0
	result_den = 0

	#here is the logic for the math.
	if tup1[1] == tup2[1]:
		result_num = tup1[0] + tup2[0]
		result_den = tup1[0]
	elif tup1[1] != tup2[1]:
		result_num = (tup1[0] * tup2[1]) + (tup2[0] * tup1[1])
		result_den = (tup1[1] * tup2[1])
	#create and return the tuple.
	return (result_num, result_den)

def malt_fraction(tup1,tup2):
	#do the math and return the tuple.
	return ((tup1[0] * tup2[0]),(tup1[1] * tup2[1]))


#print out all the info
stdout.write("the first fraction is: " + str(tup1[0]) + "/" + str(tup1[1]) + "\n")
stdout.write("the second fraction is: " + str(tup2[0]) + "/" + str(tup2[1]) + "\n")

temp = add_fraction(tup1,tup2)
stdout.write("the result of the addition is: " + str(temp[0]) + "/" + str(temp[1]) + "\n")
#delete temp so i can use it again.
temp = None
temp = malt_fraction(tup1,tup2)
#print the new number information
stdout.write("the result of the maltiplication is: " + str(temp[0]) + "/" + str(temp[1]) + "\n")

