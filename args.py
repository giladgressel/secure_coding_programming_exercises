"""
Let's learn about *args

"""

a = "hi"
b = "I  am the debugger"
c = a + " " + b
print(c)


def sum_stuff(*args):
    """
    lots_of_ints : will be some kind of container
    """
    total = 0
    for elem in args:
        total += elem
    return total


my_list = [
    2,
    4,
    5,
    6,
]
print(sum_stuff(*my_list, 10, 11, *my_list, *my_list))
l_comp = [i for i in range(10)]
print(sum_stuff(*[i for i in range(10)]))


def my_sum(a, b):
    return a + b


print(my_sum(10, 10))

