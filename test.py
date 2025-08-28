rows = int(input("Enter desired number of rows: "))

for i in range (1,rows+1,1):
    for j in range (1,i+1,1):
        print("+",end="")
    print ()    #terminates row