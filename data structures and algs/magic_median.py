def magic_median(L, start, end, k):
    if end < start:
        return

    # BASE CASE: if length <= 120, find kth smallest by hand
    if len(L) <= 120:
        return sorted(L)[k - 1]

    # RECURSIVE CASE
    pivot = get_pivot_position(L, start, end)
    index = separate(L, start, end, pivot) - start
    #len_less = index + 1

    # recurse on the first part of the list
    if index + 2 > k: 
        return magic_median(L, start, start + index, k)
    # recurse on the second part of the list
    elif index + 2 < k: 
        return magic_median(L, start + index + 2, end, k-(index + 2))
    else:
        return L[start + index + 1]



def get_pivot_position(L, start, end):
    medians = []

    # Make groups of 5
    for i in range(start, end+1, 5):
        group_end = min(i+4, end) # has to be minimum for the last group
        group = L[i:group_end+1]
        #print(group)

        # get median by hand
        group.sort()
        group_median = group[(len(group) - 1) // 2]
        medians.append(group_median)

    # Get the median of medians by recursing on the magic median alg
    median_of_medians = magic_median(medians, 0, len(medians) - 1, (len(medians) - 1) // 2)
    return L.index(median_of_medians)


# Modified to have a pivot index
def separate(L, start, end, pivot_index):
    # Swap pivot with the end
    pivot_value = L[pivot_index]
    L[pivot_index] = L[end]
    L[end] = pivot_value

    # Perform regular separate algorithm!
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


# Concrete testing (lst of length 121)
lst = [9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
print((len(lst) - 1) // 2)
print("Kth element: ", magic_median(lst, 0, len(lst) - 1, 1))

lst = [244, 1081, 815, 21, 949, 598, 855, 114, 225, 609, 1088, 387, 478, 68, 666, 760, 185, 691, 66, 1129, 875, 126, 1144, 218, 1118, 1193, 951, 611, 535, 912, 737, 320, 255, 368, 424, 894, 1096, 389, 766, 334, 1060, 466, 129, 1197, 110, 299, 919, 1142, 5, 1022, 773, 1083, 152, 939, 1174, 323, 1157, 843, 249, 594, 603, 108, 194, 1183, 229, 13, 1064, 8, 402, 656, 1205, 333, 1045, 835, 927, 551, 316, 599, 640, 1203, 82, 312, 679, 282, 1123, 725, 571, 580, 85, 629, 1040, 659, 898, 531, 1, 1140, 907, 1059, 1036, 1012, 248, 653, 237, 10, 947, 794, 859, 744, 802, 565, 495, 897, 79, 964, 690, 397, 1095, 155, 302, 528, 326]
lst.sort()
median = (len(lst) - 1) // 2
print("WANT TO GET: ", lst[median])
print("magic median: ", magic_median(lst, 0, len(lst) - 1, (len(lst) + 1) // 2))
