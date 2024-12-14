'''
when you have a specific number to repeat the same process, 
you can use a for loop.
'''

# print 10 digits from 0 to 9
print("From 0 to 9")
for each in range(0, 10, 1):
    print(each)

# print 10 digits from 2 to 7
print("From 2 to 7")
for each in range(2, 8, 1):
    print(each)

# print all the even numbers between 3 and 10
print("Evens between 3 and 10")
for each in range(3, 11, 2):
    print(each)

# multiplication tables by using nest for loops
for dan in range(2, 10, 1):
    print("_______", dan, "________")
    for each in range(1, 10, 1):
        print(dan, "*", each, " = ", dan*each)


# double the value of each element in the given list 
given = [1,2,3,4,5,6,7,8,9]
newList = list()
for each in given:
    newList.append(each*2)
print(newList)      #[2, 4, 6, 8, 10, 12, 14, 16, 18]


# print out all the keys in dictionary
d = {"Sky":123, "Level":345, "Tree":1225}
for each in d:
    print(each)

# print out all the keys by using d.keys()
for each in d.keys():
    print(each)

# print out all the values
for each in d.values():
    print(each)

# print out all the items
for each in d.items():
    print(each)