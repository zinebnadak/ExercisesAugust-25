#Write a program that calculates price for calling. Program will intake how many minutes someone calls per month and how much it costs per minute . You´ll get 10% discount if you call for at least 30 Euros
# code will:
#Takes call duration in minutes
#Lets user know cost per minute
#Applies 10% discount if total is 30 Euros or more

minutes_called = float(input ("(0.20 €/minute) Enter the number of minutes you called this month: "))

cost = minutes_called * 0.20

if cost >= 30:
    discount = cost * 0.10
    cost = cost - discount
    print (f"You've recieved a 10% discount of:{discount:.2f} €")

print (f"Total price: {cost:.2f}€")

#In a gym you can either buy a year-card or a one-time-ticket. Write a program that reads the price for a year-card, prie for a one-time-tic and the amount of times one intend to train under one year. The program will tell you if it is worth buying a year-card or not
print()
print("PRICE CHART:\nYear-card: 300€\nOne-Time-Ticket: 10€\n")
times = int(input("How many times do you intend to workout this year?: "))

year_card = 300
one_time = 10
one_time_total = one_time * times

if year_card<one_time_total:
    print (f"It is worth buying the year-card for {year_card} €")
elif year_card>one_time_total:
    print (f"It is cheaper to buy one-time tickets for {one_time_total} € total")
elif year_card==one_time_total:
    print ("Both options cost the same. Choose based on convinience")
else:
    print ("invalid input. Please enter a positive whole number!")

#Leap years are years that are evenly divisable by 4, with the exception of those that are evenly divisable by 100. However those years that are evenly divisable by 400 are leap years. Write a program that lets user input a year and prints if it is a leap year or not:
print ()
year = int(input("Enter a year:"))

if (year % 4==0 and year %100 !=0) or year % 400 ==0:
    print(f"{year} is a Leapyear!")

else:
    print (f"Sorry, {year} is not a Leapyear")

# A mobile operator offers three different subscriptions: Basic, Normal, and Plus. When comparing the conditions for the subscriptions, it turns out that the subscription Kontant is cheapest if you call at most 33 minutes per month, Normal is most profitable if you call between 33 and 66 minutes per month, and Plus is most advantageous if you call even more. Write a program that reads the number of minutes you estimate you will call per month. The program should state which subscription you should choose.
print()
minutes = int(input("Approx. how many minutes do you intend to use per month?: "))

if minutes <= 33:
    print ("Buy a Basic package!")
elif minutes >= 33 and minutes <=66:                #use "and" not "or" to get inside range!
    print ("Buy a Normal package!")
elif minutes > 66:
    print ("Buy a Plus package!")

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

#Write a program that reads in integers n and calculates sum, 1+4+9+16+...+n^2
print()
n = int(input("Enter value of n: "))

sum = 0
k = 1

while k <= n:
#new values for sum and k:
    sum=sum+(k*k)           #add square of k to the current value of sum)
    k=k+1
print ("The sum is", sum)

#Suppose a ball is dropped onto a floor and with each bounce it loses 30% of its height. Write a program that calculates how many times such a ball bounces before it comes to rest. (By “comes to rest,” we mean that it no longer bounces higher than 1 cm.) As input, the program should let the user specify the height, measured in meters, from which the ball is dropped.
height = float(input("Enter the height you are trowing the ball from (in meters):" ))

start_height = height   # Save the initial height before it changes to use it in print at the end
times_bounced = 0  #start from 0 bounced

while height >= 0.01:      #keep looping and register bounces and stop when height is 1 cm
    times_bounced = times_bounced +1
    height = height*0.7

print (f"If you drop a ball from {start_height} meters it will bounce {times_bounced} times, before stopping. ")


#Write a program that reads in the last integer( n) and calculates sum, 1+4+9+16+...+n^2, but this time use for-loop instead of while loop.

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

for i in range (1,rows+1,1):
    for j in range (1,i+1,1):
        print("+",end="")
    print ()    #terminates row

#Now reverse it : desired number of rows = number of "+" signs to be printed on first line