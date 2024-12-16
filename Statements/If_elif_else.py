'''
if(condition):
    statement
elif(condition):
    statement
elif(condition):
    statement
else:
    statement

If the condition is true, the statement will be executed. 
Otherwise, it will pass and try another existing condition.
Since a computer needs to know what to do when an error occurs,
it is important to cover the possible expections by using else.
'''

l = [1,2,3,4,5,6,7,8,9,10]
for each in l:
    if each % 2 == 0:
        if each % 5 == 0:
            print(each, " : multiples of ten")
        else:
            print(each, " : multiples of two")   
    elif each % 3 == 0:
        print(each, " : multiples of three")
    elif each % 2 == 0 and each % 5 == 0:
        print(each, " : multiples of 10")
    else:
        print(each, " : otherwise")



