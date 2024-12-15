# write a file
f = open("./Sample.txt", mode="w")
f.write("It is time for us to go home and have a dinner")
f.close()           # it is important to close it after use

# read a file
readF = open("./Sample.txt", mode="r")
print(readF.readline())
