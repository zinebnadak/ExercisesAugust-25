
#1 Write a program describing Fibinaccis number sequence, where each number is the sum of the two preceding ones.
n = int (input("How many numbers of fibonacci would you like?: "))

fibonacci_seq= [0,1]       #create new list, start with the two first

for i in range (2,n,1):     #i counts with index
    next_number = fibonacci_seq [i-2]+fibonacci_seq[i-1]    #take the two previous indexes from position "i" and add them
    fibonacci_seq.append(next_number)

print (fibonacci_seq)


#2 Program that will ask uer to write words, count how many words user wrote, tell first word and last word
words = input("Enter some words: ").split()

print (f"You wrote {len(words)} words ")
print (f"First word was {words[0]}")        #first
print (f"Last word was {words[-1]}")       #To print the last word, you should access it using the index -1

#3 Write program that read in integres and tell you how many are less than 0
integers = input("Enter some integers: ").split()   #split only work on string

integer = [int(i) for i in integers]     # convert each to integer by list comprehension in Python, and the square brackets ([ ]) are used to create a new list.

integers_less_than_zero = []
counter = 0

for num in integer:
    if num<0:
        integers_less_than_zero.append(num)
        counter = counter + 1

print (f"Integers less than zero are {counter} :{" , ".join(str(num) for num in integers_less_than_zero)}")
# str(num) converts each number to a string.
# ' '.join(...) combines them into one string with spaces (or commas, if you prefer).
# No more [], because we’re printing a formatted string, not the actual list object.

#4 Write a program that creates list with 100 random integers in intervall 1-1000. The program will then print the smallest and biggest number and calculate the two numbers average.
import random

num = [random.randint(1, 1000) for i in range (100)]           #create list with random numbers from 1-1000, let i run over it 100 times

#smallest
min(num)

#biggest
max(num)

#average
average = ((min(num)+max(num))/2)

print (f"List:{" , ".join(str(i) for i in num)}\nSmallest number:{min(num)}\nBiggest number:{max(num)}\nAverage:{average}")


