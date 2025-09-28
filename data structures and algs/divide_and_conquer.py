# Problem 4
def merge_sort(my_list, start_index=None, end_index=None):
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(my_list) - 1

    if start_index < end_index:
        mid = (start_index + end_index) // 2  # Integer division rounds down

        # Recursively sort the left and right sublists
        merge_sort(my_list, start_index, mid)
        merge_sort(my_list, mid + 1, end_index)

        # Merge the sorted sublists
        merge(my_list, start_index, mid, end_index)


def merge(my_list, start_index, mid, end_index):
    left_size = mid - start_index + 1
    right_size = end_index - mid

    # Create temporary lists to hold the left and right sublists
    left_list = my_list[start_index:mid + 1] + [float("inf")]
    right_list = my_list[mid + 1:end_index + 1] + [float("inf")]

    i = j = 0

    # Merge the two sublists back into my_list
    for k in range(start_index, end_index + 1):
        if left_list[i] <= right_list[j]:
            my_list[k] = left_list[i]
            i += 1
        else:
            my_list[k] = right_list[j]
            j += 1

# Problem 5
def max_subarray_sum(my_list, start_index=None, end_index=None):
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(my_list) - 1

    stack = [(start_index, end_index)]
    max_sum = float("-inf")

    while stack:
        start, end = stack.pop()

        # Make sure that indices are valid
        if start > end:
            continue

        mid = (start + end) // 2

        # Recursively find max subarray sums in left and right subarrays
        stack.append((start, mid - 1))
        stack.append((mid + 1, end))

        # Find the maximum subarray sum that spans the two halves
        max_intersection = max_intersection_sum(my_list, start, mid, end)

        # Update the overall maximum
        max_sum = max(max_sum, max_intersection)

    return max_sum if max_sum > 0 else 0
    

def max_intersection_sum(my_list, start_index, mid, end_index):
    left_sum = float("-inf")
    current_left_sum = 0

    # Find the maximum sum of the left part
    for i in range(mid, start_index - 1, -1):
        current_left_sum += my_list[i]
        left_sum = max(left_sum, current_left_sum)

    right_sum = float("-inf")
    current_right_sum = 0

    # Find the maximum sum of the right part
    for i in range(mid + 1, end_index + 1):
        current_right_sum += my_list[i]
        right_sum = max(right_sum, current_right_sum)

    # Update max_sum if both left_sum and right_sum are positive
    if left_sum > 0 and right_sum > 0:
        return left_sum + right_sum
    else:
        # If either left_sum or right_sum is not positive, return the maximum of the two
        return max(left_sum, right_sum)
