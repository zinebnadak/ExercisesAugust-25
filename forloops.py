#For-loops

#1 Write a program that reads in the last integer (n) and calculates sum, 1+4+9+16+...+n^2, but this time use for-loop instead of while loop.
n = int(input("Enter value of n, to calculate sum of squares from 1-n: "))
sum = 0

for i in range (1,n+1,1):  #here it actually starts from 1 and not 0 when run
    sum = sum + (i*i)
print(f"Sum of squares from 1 to {n} is: {sum}")

#2 For loop: the program calculate the value of the expression 2*(x**2)-5*x+1 for each value of x in the range -10 to 10, and prints result in a neat way.
print (f"{"x":<4}{"Result":<10}")
for x in range (-10,11,1):
    result = 2*(x**2)-5*x+1
    print (f"{x:<4}{result:<10}")

#3 While loop: the program calculate the value of the expression 2*(x**2)-5*x+1 for each value of x in the range -10 to 10, and prints result in a neat way.

print (f"{"x":<10}{"Result":<10}")
x = -1.1            #start from -1.1 bcs loop immediately adds 0.1, so the first value of x printed is -1.0.
while x<0.9:           #end at 1.0
    x = x+0.1
    result = 2 * (x ** 2) - 5 * x + 1
    print(f"{x:<10.2f}{result:<10.2f}") #increase x before printing makes you need to make from -1.1 instead of -1.0, and 0.9 istead of just 1.0

#compare
print (f"{"x":<10}{"Result":<10}")
x = -1.0            #start from -1
while x<1.0:           #end at 1.0
    result = 2 * (x ** 2) - 5 * x + 1   #OBS! always need to define terms BEFORE printing
    print(f"{x:<10.2f}{result:<10.2f}")
    x = x+0.1          #runs one time THEN adds 0.1


#4. Nested loops: program that lets user choose number of rows that are going to be printed and for every row prints one more "+" sign is going to be printed, starting with one "+" sign at row one.
rows = int(input("Enter number of rows to be printed: "))

for i in range (1,rows+1,1):      # range controls number of rows. Includes start but excludes stop thats why you need +1
    for x in range (1,i+1,1):     # range controls "+" signs printed, depends on the row number
        print ("+", end="")     # end="" prints plus without newline, bcs print automatiallt creates a new line
    print()                     # after finishing a row, first NOW go to new line

#5 Now reverse it : desired number of rows = number of "+" signs to be printed on first line
rows = int(input("Enter number of rows to be printed: "))

for i in range (rows+1,1,-1):      # range controls number of rows.
    for x in range (1,i,1):     # range controls "+" signs printed, depends on the row number,not now it prints i-1 number of "+" signs. bcs when i = rows+1 in outer loop, the inner loop prints (rows+1)-1 = rows plus signs → correct first row length. Remember!: The system always includes first but excludes last, so always keep an eye on what the last number is included or not!
        print ("+", end="")     # end="" prints plus without newline, bcs print automatiallt creates a new line
    print()

#6 User gets to choose how big the number can possibly be and times of tries user gets.
# Program "thinks" of a random number within 1 and the users choice.
# User must guess number.
# If user guesses too big or too little the program will let user know.
# Check if the user has won or run out of attempts: The program will stop once the user guesses the correct number or runs out of tries.
# OBS! Ensure that the feedback only happens before the last attempt. After the last attempt, the program will simply print the "Sorry, you've run out of attempts" message without repeating any feedback.

import random

max_num = int(input("Enter the maximum number (from 1 to...): "))
max_tries = int(input("Choose number of tries?: "))

number = random.randint(1, max_num)

guess = int(input("Guess the number! "))

for i in range(0, max_tries, 1):
    if guess < 1 or guess > max_num:
        guess = int(input(f"Please enter a number between 1-{max_num}: "))
        continue
    elif guess < number:
        print(f"The number is bigger! Attempts left {max_tries-(i+1)}/{max_tries}")
    elif guess > number:
        print(f"The number is smaller! Attempts left {max_tries-(i+1)}/{max_tries}")
    else:
        print(f"Congratz! You are right! The number was {number}!")
        break

    if i != max_tries-1:  # Only ask for another guess if attempts remain
        guess = int(input("Guess again! "))

else:  # Ran out of tries
    if guess != number:
        print(f"Sorry, you're out of tries. The number was {number}.")


#7


