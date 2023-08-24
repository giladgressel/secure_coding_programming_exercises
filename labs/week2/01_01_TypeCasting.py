# Type Casting Exercise

a = 7

# 1. print the type of the variable
print("case1: ",type(a))
#   Convert integer variable to float and confirm the type cast worked (print it out)
a=float(a)
print("case2: ",type(a))
# 2. Now, Convert your float variable to string and print out the type
a=str(a)
print("case3: ",type(a))

# 3. Finally, Convert your string variable back to integer and print it out (the type)
a=float(a)      #need to convert to float first, as string of a number with decimal point cannot be converted to integer
a=int(a)        #finally we can convert the float value to an integer
print("case4: ",type(a))
