# Finding the Square Root of an Integer

To find the floor square root function, I used a binary search algorithm to cut the possiblity of answers by n/2 through each iteration. This allowed a time efficiency of O(log(n)). Since I used only temporary variables, the amount of memory needed did not vary depending on the input size; thus leading to a space complexity of O(1).