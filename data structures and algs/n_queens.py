import random

# Problem 1
def get_perms(n, k, solutions=None, candidate=None):
    if candidate is None:
        candidate = []
    if solutions is None:
        solutions = []

    # test the candidate.
    ###########################
    if len(candidate) == k:
        solutions.append(candidate[:])

    else:
        # generate extensions.
        ######################

        extensions = [i for i in range(n) if i not in candidate]

        # process new candidates.
        #########################
        for extension in extensions:
            candidate.append(extension)
            get_perms(n, k, solutions, candidate)
            candidate.pop()

    return solutions


# Problem 2
def make_sum(L, goal, solutions=None, candidate=None):
    if candidate is None:
        candidate = []
    if solutions is None:
        solutions = []

    # test the candidate.
    ###########################
    if len(candidate) == len(L):
        candidate = [L[i] for i in range(len(candidate)) if candidate[i] == 1]
        if sum(candidate) == goal:
            solutions.append(candidate[:])

    else:
        # generate extensions.
        ######################
        extensions = (0, 1)

        # process new candidates.
        #########################
        for extension in extensions:
            candidate.append(extension)
            make_sum(L, goal, solutions, candidate)
            candidate.pop()

    return solutions


# Problem 3: Eight Queens
def check_validity(candidate):
    for i in range(len(candidate)):
        for j in range(i + 1, len(candidate)):

            # check if they are in the same row
            if candidate[i][0] == candidate[j][0]:
                return False

            # check if they are in the same column
            if candidate[i][1] == candidate[j][1]:
                return False
                
            # check if they are in the same diagonal
            if abs(candidate[i][0] - candidate[j][0]) == abs(candidate[i][1] - candidate[j][1]):
                return False
    return True

def pretty_print_board(solution):
    n = len(solution)
    for i in range(n):
        for j in range(n):
            if (i, j) in solution:
                print('Q', end = " ")
            else:
                print('*', end = " ")
        print()

def queens(n, candidate=None):
    if candidate is None:
        candidate = []

    # test the candidate.
    ###########################
    if len(candidate) == n:
        if check_validity(candidate):
            pretty_print_board(candidate)
            quit()

    else:
        # generate extensions.
        ######################
        extensions = [(i, j) for i in range(n) for j in range(n) if (i, j) not in candidate]

        # process new candidates.
        #########################
        for extension in extensions:
            candidate.append(extension)
            queens(n, candidate)
            candidate.pop()
