# How to make an empty dictionary
d = dict()
d = {}

# How to initialize a dinctionary
d = {"Sun":1212, "Flower":1234}

# How to get a list of keys
d.keys()
# How to get a list of values
d.values()
# How to get a list of items
d.items()

# How to add a new element to the dictionary
d.update({"Universe" : 0000})
print(d)

# How to get an value corresponding to its key
print(d["Flower"])
print(d.get("Sun"))

# If the new element is not in the dictionary, it will be added.
# Otherwise, its value will be updated
d["Sun"] = 1999
d["Moon"] = 1989
print(d) 

print(d.pop("Sun"))
print(d)


print(d.popitem())
print(d)
