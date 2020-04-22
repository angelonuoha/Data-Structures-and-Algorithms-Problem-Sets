'''
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

'''

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Return the number if it is 0 or 1
    if number == 0 or number == 1:
       return number
    elif number < 0:
       return None

    bottom_val = 0
    top_val = number
    
    # Search for the square root through guess and check and narrowing the list by n/2 each time.
    while bottom_val <= top_val:
       mid_val = (top_val + bottom_val) // 2
       if mid_val ** 2 == number:
          return mid_val
       elif mid_val ** 2 > number:
          top_val = mid_val
       elif mid_val ** 2 < number:
          bottom_val = mid_val
          if mid_val ** 2 < number < (mid_val + 1) ** 2:
             return mid_val


# 'Pass' Test Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-2)) else "Fail")

# 'Fail' Test Cases
print ("Pass" if  (5 != sqrt(16)) else "Fail")
print ("Pass" if  (30 != sqrt(9345)) else "Fail")
print ("Pass" if  (4 != sqrt(27)) else "Fail")