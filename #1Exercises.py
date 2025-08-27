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