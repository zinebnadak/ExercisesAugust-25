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





