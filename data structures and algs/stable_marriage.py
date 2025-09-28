# A simple stack implementation

class Stack:
    # attributes:
    #    array

    def __init__(self, array=[]):
        self.array = array

    # Insert a value to the stack at the end of the array
    def push(self, value):
        self.array.append(value)

    # Pop out the last item
    def pop(self):
        return self.array.pop()

    # Checks if the Stack is empty
    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False


# Make list of lists where the index is a man and the value is a list
# where the number at index i is that man's ranking for woman i
def make_men_list(men_prefs, n):
    lst = []
    for i in range(n):  # loop through men
        new_list = []
        for j in range(n):  # loop through women
            for k in range(n):
                if men_prefs[i][k] == j:
                    new_list.append(k)
        lst.append(new_list)

    return lst


# Make a list of lists where the index is a woman and the value is a list
# that is backwards of the woman's preferences
def make_women_list(women_prefs, n):
    lst = []
    for i in range(n):
        woman_list = [women_prefs[i][j] for j in range(n-1, -1, -1)]
        lst.append(woman_list)
    return lst


def get_matching(women_prefs, men_prefs):
    num = len(women_prefs)
    mList = make_men_list(men_prefs, num)
    wList = make_women_list(women_prefs, num)
    m_to_w = {}  # men to women engagements
    w_to_m = {}  # women to men engagements
    # this is a stack so that everything is in constant time!
    women_stack = [i for i in range(num-1, -1, -1)]  # to get next single w

    while len(women_stack) != 0:
        singleWoman = women_stack.pop()  # get the first single woman
        currentMan = wList[singleWoman].pop()  # next man w has not proposed to

        # if the man is single
        if currentMan not in m_to_w:
            m_to_w[currentMan] = singleWoman
            w_to_m[singleWoman] = currentMan

        # if the man is engaged
        else:
            otherWoman = m_to_w.get(currentMan)  # find woman that m is engaged

            # if he stays with original engagement to otherWoman
            if mList[currentMan][otherWoman] < mList[currentMan][singleWoman]:
                women_stack.append(singleWoman)

            # if he chooses to break off engagement with otherWoman
            else:
                women_stack.append(otherWoman)
                m_to_w[currentMan] = singleWoman
                w_to_m[singleWoman] = currentMan

    return w_to_m
