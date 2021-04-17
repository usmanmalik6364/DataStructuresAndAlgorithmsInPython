# R-1.1)Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
def is_multiple(n, m):
    if m % n == 0:
        print(f"{n} is a factor of {m}")


# test 1.1 is_multiple(2, 4)

# R-1.2) Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise.However, your function
# cannot use the multiplication, modulo, or division operators.


def is_even(k):
    result = True if (-1)**k == 1 else False
    return result


# test 1.2 k = int(input("Enter the integer value to be checked for even\t"))
# print(is_even(k))

# R-1.3) Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. <em>Do not use the built-in functions min or
# max in implementing your solution.</em>

def minmax(data):
    min, max = 0, 0  # min and max = 0 at start
    if len(data) < 1:
        return None
    elif len(data) < 2:
        # min max are same if the list only contains one element
        return (data[0], data[0])
    else:
        for item in data:
            if item < min:
                min = item
            if item > max:
                max = item
    return min, max


# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(minmax(data))   prints (0,9)


# R-1.4) Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_squares(n):
    result_sum_of_squares = 0
    for x in range(n):
        result_sum_of_squares += x**2
    return result_sum_of_squares


# print(sum_squares(10))

# R-1.5) Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

result = sum([x**2 for x in range(10)])
# print(result)

# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def sum_squares_odd(input):
    result = sum([x**2 for x in range(input) if x % 2 != 0])
    print(
        f"The result of sum of squares of all odd numbers less than {input} is {result}")


# sum_squares_odd(4)

# R-1.7Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function

# Solution => Refer to line 72.

# R-1.9What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

# Solution range(50,90,10)
def problem_onePointNine():
    for i in range(50, 90, 10):
        print(i)


# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list[1, 2, 4, 8, 16, 32, 64, 128, 256].
result = [2**x for x in range(1, 9)]
# print(result)
