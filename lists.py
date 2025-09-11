fruits = ["Banana", "Orange", "Cherry", "Apple", "Berry"]

print(fruits[2])

fruits[4] = "Blueberry"
print()

print(fruits)

#Edit lists
print()
fruits.append("Kiwi") #add an item at the end of the list
print(fruits)

print()
fruits.insert(2, "Mango") #Add an item in a particular position
print(fruits)

print()
fruits.remove("Blueberry") #removes an item from the list
print(fruits)

print()
fruits.sort() #sort the list in ascending order automatically
print(fruits) 

print()
fruits.sort(reverse = "descending") #manually set the sort to descending
print(fruits)