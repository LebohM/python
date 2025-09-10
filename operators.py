# + add
# - subtract
# * Multiply
# / devide
# % modulus
# ** exponent

num = 3
num2 = 7

sum = num + num2
print(sum)

print(num * num2)

#control Statements 

if num > 5:
    print('num is a positive number')
elif num < 0:
    print('num is a negative number')
else:
    print(num)
    

#More control statements
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number1 > number2:
    print(number1, 'is greator than ', number2)
elif number2 > number1:
    print(number2, 'is greater than ', number1)
else:
    print('both numbers are equal')
 
 