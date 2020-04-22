# Dutch National Flag

In order to sort the array with time efficiency of O(n), I traversed the list once. In this iteration, I moved all of the zeroes to the front and then in the next I moved all the twos to the back. This automatically took care of the position of the ones and since I used only temporary variables, the amount of memory needed did not vary depending on the input size; thus leading to a space complexity of O(1).
