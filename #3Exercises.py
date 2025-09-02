

#Write a program that reads in integers n and calculates sum, 1+2+3+4+...+n
print()
n = int(input("Enter value for n: "))
sum = 0  #the sum is 0 in beginning
k = 1  #start from number 1, k is used to keep track of the current number in summation

while k <= n:
    #the new values of sum and k after each loop
    sum = sum + k  #adds value of k to sum
    k= k+1         #then add k (1) for next time
print ("The sum is:", sum)

---------> #Write a program that reads in integers n and calculates sum, 1+4+9+16+...+n^2
print()
n = int(input("Enter value of n: "))

sum = 0
k = 1

while k <= n:
#new values for sum and k:
    sum=sum+(k*k)           #add square of k to the current value of sum)
    k=k+1
print ("The sum is", sum)

---------> #Suppose a ball is dropped onto a floor and with each bounce it loses 30% of its height. Write a program that calculates how many times such a ball bounces before it comes to rest. (By “comes to rest,” we mean that it no longer bounces higher than 1 cm.) As input, the program should let the user specify the height, measured in meters, from which the ball is dropped.
height = float(input("Enter the height you are trowing the ball from (in meters):" ))

start_height = height   # Save the initial height before it changes to use it in print at the end
times_bounced = 0  #start from 0 bounced

while height >= 0.01:      #keep looping and register bounces and stop when height is 1 cm
    times_bounced = times_bounced +1
    height = height*0.7

print (f"If you drop a ball from {start_height} meters it will bounce {times_bounced} times, before stopping. ")

#At a very dangerous workplace, the following salary is offered: on the first day you earn 0.01 euro, and then the salary doubles each day. Write a program that calculates how long you need to work in order to earn 1 million euros.
current_day = 1
daily_salary = 0.01
total_money_earned_so_far = 0.01

while total_money_earned_so_far < 1000000:       #Use a while loop, because you don’t know in advance how many days it will take.# target = 10 million €
    current_day = current_day+1
    daily_salary = daily_salary*2       #each day the salary doubles
    total_money_earned_so_far = daily_salary + total_money_earned_so_far    #adding each day’s salary to the total.

print (f"To earn 1 000 000 euros, you would need to work {current_day} days!")

#Write similar program that lets you choose your goal, and by entering your daily salary lets you know how many days it will take you to surpass you goal
goal = int(input("How much do you aim to earn?: "))
salary = int(input("How much do you earn each day?: "))

current_day = 1
daily_salary = salary
total_money_so_far = salary

while total_money_so_far<goal:      #what will happen after every day?
    current_day = current_day +1
    total_money_so_far = total_money_so_far + daily_salary
print (f"To earn {goal} € you would need to work {current_day} days!")































---------------> #Write a program that reads in the last integer( n) and calculates sum, 1+4+9+16+...+n^2, but this time use for-loop instead of while loop.

#iterate trough the numbers from 1 to n
#square each number
#add it to a running total
print ()

n = int(input("Enter the value of n: "))

sum = 0
for i in range (1,n+1,1):               #range(1, n+1) The sequence will go up to but not including n+1. This ensures that n is included in the sequence., and by default setpes is 1
    sum= sum+(i*i)

print(f"The sum of squares from 1 to {n} is: {sum}")


#the program calculate the value of the expression 2*(x**2)-5*x+1 for each value of x in the range -10 to 10, and prints result in a neat way.
print()
print()

print (f"{"x":<4}{"Result":<10}")   #Left-align columns
for x in range (-10,11,1):
   result = 2*(x**2)-5*x+1
   print (f"{x:<4} {result:<10}")    # Print the result in a table format
print()
print()

# increment value of x by 0.1 (a float) in range -1 to 1
# because value increments by 0.1 (float) we will use a while loop and start from -1 instead of a for loop
print (f"{"x":<4}{"Result":<10}")   #Left-align columns

x= -1 #start at -1
while x <=1:      #The range() function only accepts integer values for start, stop, and step. # while will Loop until x reaches 1
   result = 2*(x**2)-5*x+1
   print (f"{x:<4.1f} {result:<10.2f}")    # Print the result in a table format
   x = x+0.1        # Increment x by 0.1

#Nested loops: program that lets user choose number of rows that are going to be printed and for every row prints one more "+" sign is going to be printed, starting with one "+" sign at row one.

rows = int(input("Enter desired number of rows: "))

for i in range (1,rows+1,1):    #prints rows, eg. this loop will run amount of times entered by user
    for j in range (1,i+1,1):   #range(1, i + 1) means that for row i (e.g., if i = 3), this loop will run from 1 to 3 (i.e., j will be 1, 2, 3).
        print("+",end="")       #one "+" one same row, during this j row
    print ()    #terminates current row, and changes to next row

#Now reverse it : desired number of rows = number of "+" signs to be printed on first line
rows = int(input("Enter desired number of rows: "))

for i in range (rows+1,1,-1):
    for j in range (1,i,1):
        print ("+",end="")
    print()

# User gets to choose how big the number can possibly be and times of tries user gets. Program "thinks" of a random number within 1 and the users choice. User must guess number. If user guesses too big or too little the program will let user know. Check if the user has won or run out of attempts: The program will stop once the user guesses the correct number or runs out of tries.
#ensure that the feedback only happens before the last attempt. After the last attempt, the program will simply print the "Sorry, you've run out of attempts" message without repeating any feedback.
import random

max_num= int(input("Enter the maximum number (from 1 to...):"))
max_tries= int(input("Choose number of tries?: "))

random_number= random.randint(1,max_num)

for attempt in range(1,max_tries+1):
    users_guess= int(input(f"Guess the number! Attempt {attempt}/{max_tries}: "))


    if users_guess < 1 or users_guess > max_num:
        print(f"Please enter a number between 1-{max_num}: ")
        continue        # Skip this iteration and and move to the next one.(eg. let the user guess again)

    if attempt == max_tries:            #The if attempt == max_tries: condition is used to check if it's the last attempt. If it is, the program only prints a message indicating whether the guess was correct or not, without giving any further "Too low" or "Too high" feedback.
        if users_guess == random_number:
            print (f"Contratulations! You´ve guessed the right number, {random_number}, in {attempt} tries!" )
        else:print (f"Sorry, you´ve run out of attempts. The correct number was {random_number}.")
        break       # Exit the loop if the user guesses correctly, and terminate program

    elif users_guess<random_number:
        print("Too low, try again!")

    elif users_guess>random_number:
        print("Too high, try again!")


#Write a program that prints a table for the numbers 1 to 12. On each row of the table, the number should be shown, as well as the number squared and the number cubed.
print ("Tal: ", "Talet i kvadrat: ", "Talet i kubik: ")
for number in range (1,13,1):
    print (f"{number:<6}{number**2:<18}{number**3:<15}")

#Write a program that displays a multiplication table according to the following model. The program should be designed so that you read in the number of rows to be printed. Tip: Use nested for-loops.
#1   2   3   4   5   6   7   8   9
#2   4   6   8  10  12  14  16  18
#3   6   9  12  15  18  21  24  27
#4   8  12  16  20  24  28  32  36
#5  10  15  20  25  30  35  40  45
#6  12  18  24  30  36  42  48  54
#7  14  21  28  35  42  49  56  63
#8  16  24  32  40  48  56  64  72
#9  18  27  36  45  54  63  72  81
rows = int(input("How many rows of numbers do you want to be printed?: "))


for i in range (1,rows+1,1):        #row+1 to include the row user wants
    for j in range (1,10,1):
        print (f"{i*j:>4}", end="")       # i*j because i tells on what row multiplied by the number place horizontally, end="" means don’t move to the next line, just keep printing on the same line.
    print()                     #moves the cursor to the next line.

#use Boo1 (Boolean).Is used when you want to check conditions (yes/no, on/off, 1/0). A Boolean is a data type that can only be True or False
#Write a program that asks the user for their age and checks if they are old enough to vote (let’s say 18+)
age = int(input("Enter your age: "))
can_vote: bool =age >= 18       #if age is greater than or equal to 18 the result is True, otherwise False
print ("Can vote?", can_vote)  #can_vote is printed in True or False (bool)

