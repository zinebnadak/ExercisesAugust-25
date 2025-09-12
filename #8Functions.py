#1 define a function that calculates the biggest of two integers
def biggest(a,b):
    if a>b:
        return a
    if b>a:
        return b

result = biggest(5,9)
print(result)

# 2 Use Bool-type: Define a function that examines if a certain year is a leap year
def leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

leap_year_input = int(input("Enter a year: "))

answer = leap_year(leap_year_input)
print(answer)