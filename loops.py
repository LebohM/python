# FOR Loop

fruits = ["Banana","Apple", "Orange", "Pineapple", "Mango"]
print(fruits)
print()

numbers = [2,4,6,9]
print(numbers)
print()

for f in fruits:
    print(f)

print()
  
for n in numbers:
    print(n)
    

#While Loop
print()
c = 1

while c <= 5:
    print(c)
    c += 1 #increment
    
#FOR Loop Control Statements    
print()

for f in fruits:
    if f == "Orange":
        break # stops the loop
    print(f)
    
print()
for f in fruits:
    if f == "Orange":
        continue  # skips the selected value and continues with the loop to next item
    print(f)
    
print()
for f in fruits:
    if f == "Orange":
        pass #doesn't do anything prints as normal 
    print(f)
    

#WHILE Loop control Statements
