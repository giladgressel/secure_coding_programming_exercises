# Replace all occurrences of the letter `m` with the symbol `_`.
# For example:

# text: more python programming please
# symbol: #
# result: #ore python progra##ing please

poem = """10
maggie and milly and molly and may
went down to the beach(to play one day)
and maggie discovered a shell that sang
so sweetly she couldn't remember her troubles,and
milly befriended a stranded star
whose rays five languid fingers were;
and molly was chased by a horrible thing
which raced sideways while blowing bubbles:and
may came home with a smooth round stone
as small as a world and as large as alone.
For whatever we lose(like a you or a me)
it's always ourselves we find in the sea"""

# Write your code below here

        #strings are immutable so converting string to list.
        #will later convert it back to string
        
l1= list(poem)
while "m" in l1:
    l1[l1.index("m")] = "_"



updated_poem = ""           #converting back to string. i think there might be a more efficient way though..
for i in l1:
    updated_poem+=str(i)
print(updated_poem)         #printing updated string