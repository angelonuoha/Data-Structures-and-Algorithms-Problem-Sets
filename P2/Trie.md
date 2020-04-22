# Building a Trie in Python

## Suffixes Algorithm
In order to find all the suffixes in a Trie dictionary, I used a recursive function to iterate through the items of the dictionary. In each iteration, I called the function again and appended a results array with the character and suffix (in the form of a returned partial array from the recursive function). Creating a new array for every node in the children, this algorithm has a space complexity of O(n). Since we are traversing all children while building the suffixes, the time efficiency is also O(n).

## Find and Insert
For finding a Trie node that represents a certain prefix, you may need to traverse all the children, which would lead to a O(n) time efficieny in the worst case. For space complexity, we do not create any additional data structures based on the input and so it is O(1). In order to insert a word, we have to for loop through each letter in the word leading to a time efficiency of O(n) as well. For each letter, we create a new node thus leading to a space complexity of O(n).