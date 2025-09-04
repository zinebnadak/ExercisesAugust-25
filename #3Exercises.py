
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


3. Förbättra "Merry-go-round" genom att lägga till en nästlad loop så att
Programmet endast accepterar y eller n som giltig input
Om användaren skriver in annan input ska programmet skriva ut ett felmeddelande och upprepa frågan Go again? (y/n)

4. Skriv ett program som skriver ut de fem första multiplikationstabellerna (1*1 till 10*5). Använd en nästlad for-loop.

    print()
    name = "Zineb"
    chars = list(name)

    for i in range(len(chars) - 1, -1, -1):
        print(chars[i], end="")

    print()
    namn = "Mariam"
    print(namn[5], namn[4], namn[3], namn[2], namn[1], namn[0], sep="")
    # the reason your code prints with spaces is because print() by default inserts a space between its arguments.

+ i häftet

