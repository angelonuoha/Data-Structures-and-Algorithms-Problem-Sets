# Huffman Coding

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

I used a priority queue with the heapq module in Python to build the Hoffman Tree. This works by storing the weight (the frequency in which each letter occured) into each node and placing each node into a priority queue. Then I created a Min Heap and assigned each leaf a unique binary code based on the tree. The time complexity for this algoritm is O(n log n) and the space complexity is O(n), with n being the number of unique characters in the input string.