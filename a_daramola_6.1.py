#Akinola Daramola Jr
#Programming Exercise 6.1
#Due Date: 07/24/2022


"""
File Display
Assume a file containing a series of integers is named numbers.txt and
exists on the computer’s disk. Write a program that displays all of the numbers in the file.

"""

def main():
    iterate()


#number = numbers_file.readline()

def iterate():
    #Creating an object of the file numbers.txt
    numbers = open("numbers.txt", "r")
    
    #Creating a for loop to iterate through object 
    for number in numbers:
        #Displaying numbers in files
        print(number)
        
    
#Calling mainline function
main()
