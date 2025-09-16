'''
def greet(name):
    print(f"hello, {name}", '\n')
    
greet("Bianca")

def addNums(a, b):
    return a + b

results = addNums(2, 7)

print(results)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

results = factorial(4)

print(results)