# join 
s = "String"
print(s)
print(s.join("ABC"))        # AStringBStringC

#capitalize
print("i love you".capitalize())    # I love you

#center
print("I love you".center(20))      #      I love you     

#count
print("I love you, love you, love".count("l")) # 3

#endswith
print("This ends with a comma,".endswith("."))  #False
print("This ends with a period.".endswith(".")) #True

#isalpha
print("String".isalpha())       #True

#isdigit
print("14".isdigit())           #True

#isupper
print("ABd".isupper())

#lower
print("ABC".lower())

#slice
temp = "I do not know what I am going to have for dinner"
print(temp[0:20: 3])

#indexing
ss = "This is an indexing test for string types"    # s
print(ss[-1])

#reverse
t = "temp"
print(t[::-1])

# strip
target = "        I love you           "
print(target.strip())
print(target.rstrip())
print(target.lstrip())

