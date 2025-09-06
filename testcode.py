#3 write a new version of the program that finds first white space, usa a for-loop with range, and an else part

text = input("Please write a sentence: ")

for i in range(len(text)):          #Loop over the numbers from 0 up to, but not including, the length of the text." So if len(text) is 5, range(len(text)) generates the sequence: 0, 1, 2, 3, 4. These are the valid index positions of the characters in text
    if text[i] == " " or text[i] == "\t":
        print(f"First white space is on place {i+1}")
        break
else:
    print ("No white space!")

