# A classic C style array has fixed length and fixed data type
# If I'm not wrong, it's written something like this
# int x[10];

# you basically need some part to say what "type", then what "size". Other
# ways of writing this information could be:

# x = 10 integers;
# variable X = integer array of 10;
# let x = new int[10];

# Here, what happens is that we know that an int takes <S> amount of space and so we
# can get the value at any point in the array simply by using the formula
# address = start + (<S> * index)

# This let's us get to ANY element in the array in the same number of steps

# 1. what is the index?
# 2. what is the start?
# 3. what is the type size?
# 4. address = start + (size * index)

# ===================================================
# there are no arrays in python. Usually we use lists wherever we need to use arrays
# - lists have no fixed size
# - they can have any type of item in them
# - they are still constant access time
mylist = []
mylist = [1, 2, 3, "char", "paanch", 6]


# The concept of an array/list is however deeper than just this
# An array is basically some "structure" that allows you to store and get back
# "things" one after another, by labelling them with numbers.

# For example, this could be an array of size two:
def make_array(a, b):
    def lookup(
        index
    ):  # this is called a closure. You can google it later. For now it's ok to ignore this
        if index == 0:
            return a
        elif index == 1:
            return b

    return lookup


# Classically you would define a 2-array like this in Python
array = [10, 20]
# and access it like this
print(array[0])
print(array[1])

# the function we defined above also "behaves" in a similar way
array = make_array(10, 20)
print(array(0))
print(array(1))


# Try to understand the above function but don't worry if you don't! We can
# discuss that in class! Make sure to raise a question either in the telegram group though.

# So when we talk of arrays, what we are talking about is the behaviour of
# giving back "something" when being provided a number, in constant time. Whether
# it's a constant time memory lookup or just a stupid function doing that does
# not matter :-D

# Go to hackerrank.com and do some of the easy array questions. Remember, an
# array is the "behaviour" of integer->thing in constant time.

# - https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays
# - https://en.wikipedia.org/wiki/Array_data_structure
