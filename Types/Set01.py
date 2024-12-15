# How to make an empty set
s = set()

# How to initialize a set
s01 = {1,2,3,4,5} 
s02 = {3,4,5,6,7}

# union
print(s01.union(s02))

# difference
print(s01.difference(s02))
print(s01 - s02)

# intersection
print(s01.intersection(s02))


'''
pop : the order of the elements can vary. 
Therefore, the result could not be always the same. 
'''
s03 = {'a', 'b','c'}
print(s03.pop())