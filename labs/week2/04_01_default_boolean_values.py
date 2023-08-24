# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
an_int = int()
# a float
a_float = float()
# a string
a_string = str()
# the int 0
int_0 = 0       #no need for casting type as python would do that in the background
# the int 1
int_1 = 1
# the int 1000
int_1000 = 1000

# now print out all the `bool()` values using the bool() function
print(bool(an_int))
print(bool(a_float))
print(bool(a_string))
print(bool(int_0))
print(bool(int_1))
print(bool(int_1000))
# are you surprised at the default boolean value for any python type?


        #i am, actually i didint expect this output.
        # I am assuming all empty or zero values in float or integer, are considered false.
        #And everything else is true