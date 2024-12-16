'''
The sequences should have the same length.
'''
l01 = [1,2,3,4]
l02 = ['a', 'b', 'c', 'd']
newList = list(zip(l02, l01))
print(newList)
newDict = dict(zip(l02, l01))
print(newDict)
newTuple = tuple(zip(l02, l01))
print(newTuple)
