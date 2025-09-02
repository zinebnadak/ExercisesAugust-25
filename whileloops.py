#1 #Write a program that reads in integers n and calculates sum, 1+2+3+4+...+n

n = int(input("Enter value of n: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print (f"Sum of integers up to {n} is {sum}")

#2 Write a program that reads in integers n and calculates sum, 1+4+9+16+...+n^2
print()

n = int(input("Enter value of n: "))

sum = 0
z = 1

while z <= n:
    sum = sum+(z*z)
    z = z+1

print (f"Sum of squared integers up to {n} is {sum}")

#3 Suppose a ball is dropped onto a floor and with each bounce it loses 30% of its height. Write a program that calculates how many times such a ball bounces before it comes to rest. (By “comes to rest,” we mean that it no longer bounces higher than 1 cm.) As input, the program should let the user specify the height, measured in meters, from which the ball is dropped.
height = float(input("Enter the height the ball is dropped from (in meters): "))
original_height = height # save the starting height so that When you run your code, you’re not printing height at the end
bounces = 0

while height >= 0.01:
    height = height * 0.70
    bounces = bounces + 1

print(f"If you drop a ball from {original_height} it will bounce {bounces} times before stopping!")


#4 Write a program that lets you choose your goal, and by entering your daily salary lets you know how many days it will take you to surpass you goal
salary = float (input("Enter your daily salary: "))
goal = float(input("Enter your goal: "))

current_day = 1
total_money_so_far = salary

while total_money_so_far<goal:
    total_money_so_far=total_money_so_far+salary
    current_day=current_day+1

years=current_day // 365
days=current_day % 365

print(f"For you to reach {goal}€, you´ll have to work {years} years and {days} days!")











#+ se on några av "merforwhile" filen kan lösas med while