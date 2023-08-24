# 1) Initialize variable a to true, b to false and c to true
a=bool(1)     
b=bool(0)
c=bool(1)

# 2) If you print(a and b or c) what it will return? Why?
# Does the order of operations matter?
print("'a and b or c' returns",a and b or c,", because even though 'a and b' returns false, 'false or c' returns true")

# 3) Is print(a or b and c) different?
print("No, it will still return",a or b and c)

# 4)Assign c to false and print the value of a and b or c
c=bool(0)       #Assigning c to false
print("Now the value for 'a and b or c' would be",a and b or c)

# Understand the difference in each scenario
        #yes i understand
# What is happening here?
        #the code is interpreted from left to right


# 5) Now try to use some ()'s to force python to evaluate it differently.

        #if i want a different evaluation for  'a and b or c'
        #i would write a and (b or c). but for this to work,
        # the value of b has to be true and the value of a and c have to be false
        #For example:
a=(bool(0))
b=(bool(1))
c=(bool(0))
print("Without brackets: ", a and b or c)        #This would return True
        #But,
print("With brackets: ", a and (b or c))        #This would return False
        