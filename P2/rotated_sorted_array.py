'''
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
'''

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) <= 0:
        return -1
    bottom = 0
    top = len(input_list) - 1
    pivot_point = 0

    if number == input_list[0]:
        return 0
    elif number == input_list[top]:
        return top
    

    while bottom <= top:
        pivot_point = (bottom + top) // 2
        if input_list[0] < input_list[top]:
            pivot_point = 0
            break
        elif input_list[top] < input_list[top - 1]:
            pivot_point = top
            break
        elif input_list[pivot_point] < input_list[pivot_point - 1]:
            if number == input_list[pivot_point]:
                return pivot_point
            break
        elif input_list[bottom] < input_list[pivot_point]:
            bottom = pivot_point

        elif input_list[bottom] > input_list[pivot_point]:
            top = pivot_point

    bottom = 0
    top = len(input_list) - 1
    if number > input_list[bottom]:
        top = pivot_point
    else:
        bottom = pivot_point

    while bottom <= top:
        mid_index = (bottom + top) // 2
        if number == input_list[mid_index]:
            return mid_index
        elif number < input_list[mid_index]:
            top = mid_index - 1
            if top == number:
                return top
        elif number > input_list[mid_index]:
            bottom = mid_index + 1

    return -1
        


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])

test_function([[600, 700, 800, 100, 200, 300, 400], 80])
test_function([[600, 700, 800, 100, 200, 300, 400], 800])
test_function([[600, 700, 800, 100, 200, 300, 400], 0])