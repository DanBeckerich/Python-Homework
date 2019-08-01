#written by Daniel Beckerich
#on 11/16/2017
#this program is designed to read a file, and print some information

#open the file
file = open("test data.txt", "r")

#create an array of lines
lineArray =file.read().split('\n')
#this count variable will be used to keep track of which line we are on.
count = 0
for i in lineArray:

    #skip the first line.
    if count != 0:
        #create a temp variable. I use it to store each word in the line.  this also lets me use len(temp) to determin the number of words in the line.
        #A word in this context is defined as a group of letters seporated from other letters by a space.
        temp = lineArray[count].split(" ")
        print("Line Number: " + str(count + 1))
        print("Numer of words: " +str(len(temp)))
        print("Line of text: " + lineArray[count])
        print()
    #if we are going to skip the line, tell the user
    if count == 0:
        print("skip the first line")
        print()
    #increment the count.
    count += 1


#dont forget to close the file
file.close()
