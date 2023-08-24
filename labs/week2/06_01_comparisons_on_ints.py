# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
if a > b:
    print("a is bigger")
elif b > a:
    print("b is bigger")
else:
    print("a is equal to b")

# What is smaller , c or d?
c = 2.02
d = 2.01119999

if c < d:
    print("c is smaller")
elif d < c:
    print("d is smaller")
else:
    print("c is equal to d")
    
# what is bigger e or f?
e = float("inf")
        #i was expecting an error here.
        # i did not know about positive infinity, now i understand
f = 12912912912091928312903713582043754302895723048957


if e > f:
    print("e is bigger")
elif f > e:
    print("f is bigger")
else:
    print("e is equal to f")

# are these equal?

g = 1.02020202020
i = 1.0202020202011111
if g == i:
    print("g is equal to i")
else:
    print("g is not equal to i")
