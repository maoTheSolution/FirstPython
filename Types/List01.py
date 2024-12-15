'''
List is a class! 
Therefore, there are built-in functions you can use.
'''

# How to make an empty list
l = list()
l = []

# How to initialize a list
l = [1,2,3,4,5,6]

# How to add new elements in a list
l = list()
l.append(1)
l.append(3)
l.append(4)             # [1,3,4]
print(l)

# How to add new elements in a list with a specific index position
l = [1,2,3,4,5,6]
l.insert(3, 100)        # [1, 2, 3, 100, 4, 5, 6]
print(l)


# How to add two lists
first = [1,2,3,4]
second = ['a','b','c']
print(first+second)

# How to extend a list
first.extend(second)
print(first)

second.extend([1,2,3,4,5,6,7,8])   # ['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7, 8]
print(second)

# How to check the length of a list
print(len(second))          # 11

# How to take an element out of the list and return it 
l = ['a','b','c', 'd']
print(l.pop())
print(l)            # ['a', 'b', 'c']

# How to remove an element without returning it
l.remove('b')
print(l)            # ['a', 'c']
