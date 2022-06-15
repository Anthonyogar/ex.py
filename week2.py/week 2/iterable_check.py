# list, set, tuple, dict
fruits = ["Orange", "Apple", "Mango", "Cashew", "Apple"]
# mr= "Anthony"
# gen = True
# print(types(fruits))
# print(fruits)

# print(dir(gen))
# print(dir(nm))
# print(dir(fruits))

print(fruits.count("Apple"))

print(fruits)
newfruits = ["tange", "Guava", "Lime"]
fruits.extend(newfruits)

print(fruits.remove("mango"))

print(fruits)

print("Cashew" in fruits)
print(fruits.index("Cashew"))

print(fruits[-1])

# start:end: step
print(fruits[:4:2]) #splicing, slicing

#