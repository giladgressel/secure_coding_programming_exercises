# can you figure out the logic here?

ay = "a"
bee = "b"

# which one is bigger?

print(ay > bee)

# why??
        #when you use the comparison operator on strings,
        #they are compared character by character to their unicode value.
         
# here is a hint: check out the ord() function
# How does python store string characters under the hood?
# look up what ord() does online and report back!
        #ord() returns the nicode value of the character