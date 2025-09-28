import time

def karatsuba(x, y):
    # if either x or y is a single dig #
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    # the size of the numbers
    size = max(len(str(x)), len(str(y)))
    half_size = size // 2

    # split the numbers into two halves
    x1, x2 = divmod(x, 10 ** half_size)
    y1, y2 = divmod(y, 10 ** half_size)

    # recurse!
    a = karatsuba(x1, y1)
    b = karatsuba(x2, y2)
    c = karatsuba(x1 + x2, y1 + y2) - a - b

    # combine the three products
    result = a * 10 ** (2 * half_size) + c * 10 ** half_size + b
    return result


# compare times
x = 7823941712934
y = 1233248

# measure the time taken by the karatsuba algorithm
start_time_karatsuba = time.time()
result_karatsuba = karatsuba(x, y)
end_time_karatsuba = time.time()

# measure the time taken by regular multiplication
start_time_regular = time.time()
result_regular = x * y
end_time_regular = time.time()

print("\nResult of Karatsuba multiplication:", result_karatsuba)
print("Karatsuba multiplication took:", end_time_karatsuba - start_time_karatsuba, "seconds")

print("\nResult of regular multiplication:", result_regular)
print("Regular multiplication took:", end_time_regular - start_time_regular, "seconds")

correct = (result_karatsuba == result_regular)
print("\nCorrect result: ", correct)
