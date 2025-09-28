import random
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

"""
Problem 2
The recurrence relation is T(n) = 2T(n/2) + θ(n), which is the same as merge sort.
It has a runtime of n log n under this pivot assumption!

Problem 3
If you are unlucky with your pivots, the runtime can get as bad as n^2.
An example of this is if the input list is [6, 5, 4, 3, 2, 1].
In this case, the pivot of L[end] is pretty unhelpful!
"""

# -----------------------------------------------------------

def quicksort(L, start, end):
    if end <= start:
        return
    index = separate(L, start, end)
    quicksort(L, start, index)
    quicksort(L, index + 2, end)

def separate(L, start, end):
    p = L[end]
    i = start - 1
    for j in range(start, end):
        if L[j] <= p:
            i += 1
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
    temp = L[i+1]
    L[i+1] = L[end]
    L[end] = temp
    return i

# Testing if estimated time complexity of n log n holds!
def test_quicksort(n):
    input_sizes = []
    execution_times = []

    for size in range(1, n + 1):
        # randomized list of numbers 1 through size
        input_list = random.sample(range(1, size + 1), size)

        # make a copy of the input list to keep the original unsorted list
        input_list_copy = input_list.copy()

        # measure time of quicksort
        start_time = time.time()
        quicksort(input_list_copy, 0, size-1)
        end_time = time.time()

        # check if the list is sorted
        assert input_list_copy == sorted(input_list)

        # record input size and execution time
        input_sizes.append(size)
        execution_times.append(end_time - start_time)

    return input_sizes, execution_times

# test quicksort on lists of numbers 1 through N
N = 1000
input_sizes, execution_times = test_quicksort(N)

# fit the curve to the data
def expected_complexity(n, a, b):
    return a * n * np.log(n) + b

params, covariance = curve_fit(expected_complexity, input_sizes, execution_times)

# plot the data points and the fitted curve
plt.scatter(input_sizes, execution_times, label='Measured Data')
plt.plot(input_sizes, expected_complexity(np.array(input_sizes), *params), 'r-', label='Fitted Curve')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Time Complexity Analysis')
plt.legend()
plt.show()

# print the fitted parameters
print(f"Fitted parameters (a, b): {params}")

# check if the estimated time complexity (n log n) holds
if params[0] > 0:
    print("The estimated time complexity is consistent with n log n.")
else:
    print("The estimated time complexity is not consistent with n log n.")

# -----------------------------------------------------------

# Yes! The running time found in problem 2 (n log n) seems to hold. 

# -----------------------------------------------------------
"""
Problem 6 (psuedocode for linear time median problem)

quickmedian(L, start, end, k)
    if L has only one element
        return the element

    randomly choose a pivot element P from L

    separate L into two sublists (using separate function)
        - elements less than or equal to P
        - elements greater than P
    
    let lengths be len_less and len_greater

    if k < len_less: 
        run quickmedian(L, start, start + len_less - 1, k)
    else: 
        run quickmedian(L, start + len_less, end, k - len_less)

"""

