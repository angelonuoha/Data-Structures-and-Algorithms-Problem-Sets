# Search in a Rotated Sorted Array

To search the rotated sorted array, I found the index at which the array was pivoted using a binary search algorithm and then narrowed down the search to a subarray within the larger sorted array. This algorithm has a time efficiency of O(log(n)) and space complexity of O(1).