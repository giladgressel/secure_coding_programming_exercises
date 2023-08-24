# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
a = 10
b = "10"

# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
b=int(b)        #you can directly perform integer operations with the integer value of b without reassigning it to b
print("Sum (a+b)=",a+b)

## Now try to convert this variable
c = "ten"
print("c=",c)
try:        #i am gonna print the error message without the code breaking
    c=int(c)
except Exception as e:
    print("Converting c to an integer is not possible.")
    print("Error:")
    print(str(e))
    
## What kind of error does python give?
## What do you think the reason is?
