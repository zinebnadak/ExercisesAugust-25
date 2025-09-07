#se övningar i bilder
#1 Write a program  that lets the user input a text and then finds the first whitespace character in the text
text = input("Please write a sentence: ")

i = 0  # used as counter

for x in text:
    if x == " " or x == "\t":
        break
    i = i + 1  # for-loop will scan all letters and spaces and if find first space break and count it to i
if i < len(text):  # if the counter is less than the length of the text (which means we found a whitespace)
    print(f"First white space on place {i + 1}")  # counts on exactly what place is the white space on?
else:
    print("No white space!")

#2 Now write a program thah instead finds the last whitesspace character in a text
text = input("Please write a sentence: ")

last_space = 0

for x, char in enumerate(text):         #enumerate gives tubple (index, character) for each iteration goes through the string character by character, i: the index (position), char: the character
    if char == " " or char == "\t":
        last_space = x                 # update position whenever we find whitespace

print (f"The last white space is at place {last_space+1} ")


#3 write a new version of the program that finds first white space, usa a for-loop with range, and an else part

text = input("Please write a sentence: ")

for i in range(len(text)):          #Loop over the numbers from 0 up to, but not including, the length of the text." So if len(text) is 5, range(len(text)) generates the sequence: 0, 1, 2, 3, 4. These are the valid index positions of the characters in text
    if text[i] == " " or text[i] == "\t":       #text[i] means: look at the character at position i in the string text.
        print(f"First white space is on place {i+1}")
        break
else:
    print ("No white space!")

#4 Write a program that translates dates  from USA style (mm/dd/yy) to swedish style (yyyy/mm/dd)


#5 Write program that reads in text. Program will delete all white spaces from text and print result. Tip! You can change a parttext with text with lenght "0"

#6 Write a program that shows current date and time like this:
#Todays date: yyyy/mm/dd
#Current time: hh:mm:ss

#7 Assume variable "a" is assigned name and personnumber for a person:
# a = "Zineb Nadak 990314-2714"
# you now nónly want to pick out the birthdate "990314" and put it into a new variable "b"

#8 Change last exercise so you get the birthdate in format dd/mm (so 14/03)

#9 Write a program that reads in a simple message consisting of at least two words. The program should then print out both how many words were written and how many characters (letters, digits, and other symbols) the message contains. You can assume that there is exactly one blank space between each word and that there are no blank spaces before the first or after the last word.

#10 Write a program that reads in a personal identity number (the ten digits without the dash in between) and determines whether the person is a man or a woman. (The next-to-last digit is odd for men and even for women.)

#11 Write a program that reads in a text and translates it into so-called “robber language.” In this language, every consonant is doubled, with an “o” inserted in between. Vowels and other characters remain unchanged. For example, the text:
#“Hej! Kom in.”
#is translated into:
#“Hohejoj! Kokomom inon.”

#12 Write a program that reads in two time points in the form tt:mm. The program should state how many minutes there are between the two time points. You can assume that the second time point always occurs after the first one, and at the latest within the following 24 hours.

#13 A personal identity number, e.g. 561231-1234, consists of ten digits. After the birthdate, the next three digits are a birth number, and the last digit is a control digit. The control digit is calculated as follows: The first nine digits of the personal identity number are multiplied alternately by 2 and 1, starting from the left. The digits in each product are then added together, and finally, all the results are summed up. The control digit is the number that needs to be added to this sum in order to make it evenly divisible by 10.
#Example:
#Personal identity number 561231123 gives the following sum:
#5 \times 2 + 6 \times 1 + 1 \times 2 + 2 \times 1 + 3 \times 2 + 1 \times 1 + 1 \times 2 + 2 \times 1 + 3 \times 2 = 10 + 6 + 2 + 2 + 6 + 1 + 2 + 2 + 6 = 37.
#(Notice that 10 counts as 1 + 0.)
#The control digit should then be 3, because 37 + 3 = 40 is divisible by 10.
#Write a program that reads in a personal identity number and checks if it is correct.



