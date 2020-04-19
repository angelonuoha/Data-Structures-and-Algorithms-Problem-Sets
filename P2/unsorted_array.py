'''
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        return None
    elif len(ints) == 1:
        return (ints[0], ints[0])

    min_val = ints[0]
    max_val = ints[0]

    for num in ints:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return(min_val, max_val)



## Test Cases
import random

test_1 = [i for i in range(0, 10)]  # a list containing 0 - 9
test_2 = [i for i in range(10, 100)]  # a list containing 10 - 99
test_3 = [i for i in range(100, 1000)]  # a list containing 100 - 999
test_4 = [i for i in range(0, 2)]  # a list containing 0 - 1
random.shuffle(test_1)
random.shuffle(test_2)
random.shuffle(test_3)
random.shuffle(test_4)

print ("Pass" if ((0, 9) == get_min_max(test_1)) else "Fail")
print ("Pass" if ((10, 99) == get_min_max(test_2)) else "Fail")
print ("Pass" if ((100, 999) == get_min_max(test_3)) else "Fail")
print ("Pass" if ((0, 1) == get_min_max(test_4)) else "Fail")
