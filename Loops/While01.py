'''
when you need to repeat the same process until a certain condition is satisfied, 
you can use a while loop. 
'''

temp = int(input("Enter any number between 0 and 10 : "))
while(temp != 7):
    print("TRY IT AGAIN")
    temp = int(input("Enter any number between 0 and 10 : "))
    
print("YOU GOT THIS!")