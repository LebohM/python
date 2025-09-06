#strings

message = 'This is a string in single quotes'
print(message)

message1 = " THIS IS A STRING IN DOUBLE QUOTES "
print(message1)

multilineString = """Bob's World 
is cool"""
print(multilineString)

#more advance string functions

print(len(message)) #print the length

print(message[0]) #prints the character at posision 0

print(message[-1])

#UPPER, lower, strip, replace

print(message.upper())
print(message1.lower())
print(message1.strip())
