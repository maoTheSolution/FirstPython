# List calculcation
l = [1,2,3,4]
r = [6,7,8,9]
print(l+r)
print(len(l+r))


# Set calculation
s = {1,2,3,4,5}
x = {1,3,5,7}
print(s-x)
print(s.union(x))

# Tuple calculation
t = (1,2,34)
e = (5,6,7,34)
print(t+e)

# String calculation
s = "i am a string"
print(s)
print(len(s))           # print out the length of string
print(s[0])
print(s[5])
print(s[4])             # print out the character with the 4th index
print(s[-1])            # print out the last character
print(s[2:6])           # print out strings from the index 2 to 5
print(s[::2])           # print out all the elements with an even index
print(s + ", I know")
print(s[:-1])
print(s.count('g'))
print(s.replace('a', 'A'))
print(s.capitalize())
print(s.split(' '))
