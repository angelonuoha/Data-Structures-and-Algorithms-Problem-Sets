'''
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

'''

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list
        
    input_list = reverse_sorted_list(input_list)
    first_num = ""
    second_num = ""
    for i in range(0, len(input_list), 2):
        first_num += str(input_list[i])

    for i in range(1, len(input_list), 2):
        second_num += str(input_list[i])
    
    result = [int(first_num), int(second_num)]
    return result

def reverse_sorted_list(arr):
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2

    left = reverse_sorted_list(arr[:mid_index])
    right = reverse_sorted_list(arr[mid_index:])
    
    return merge(left, right)


def merge(list1, list2):
    left = 0
    right = 0
    output = []

    while left < len(list1) and right < len(list2):
        if list1[left] > list2[right]:
            output.append(list1[left])
            left += 1
        else:
            output.append(list2[right])
            right += 1

    output += list1[left:]
    output += list2[right:]

    return output


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 9, 8], [98, 9]])
test_function([[9, 8], [9, 8]])
test_function([[8], [8]])