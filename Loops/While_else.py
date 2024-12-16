'''
while(condtion):
    statement

As far as the condition is true, the statement will be executed continuously.

'''
con = True
cont = 0
while(con):
    if(cont < 10):
        print("SE")
        cont = cont + 1

    if(cont % 5 == 0):
        con = False
        break
else: 
    print("The while loop stopped without its break")


# password checker
myPW = "1234" 
count = 0
while(myPW != input("Enter your password : ")):
    if(count < 5):
        print("Try it again")
        count = count + 1
    else :
        print("Please wait for 1 minute")
        count = 0
else:
    print("Welcome.")