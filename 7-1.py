#Written by Daniel Beckerich
#on 12/2/2017
#for exercise 35 of chapter 7
#This program is designed to use a forloop to reverse a given string.

#im using this library so i get full control over the consol.
from sys import stdout

#the test data
test_string = "this is a test string!"

#function defenition
def reverse(S):
	Si = ""
	#create a range starting from the length of the word, and counting backward.
	for i in range(len(S),0,-1):
		#append the letter to the output variable.
		Si = Si + S[i-1]
	return Si

#output the information
stdout.write("Before reversing: ")
stdout.write(test_string + "\n")

stdout.write("After being reversed: ")
stdout.write(reverse(test_string) + "\n")