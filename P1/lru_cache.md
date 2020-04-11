# LRU Cache

For creating the LRU cache, I decided to use a Hash Map to store the key/value pairs in the cache and a Double Ended Queue to store the order in which those key/value pairs were used. 

I decided to implement a Double Ended Queue because this would allow me to quickly add and remove the key/value pairs to the ends of the queue with constant time.

The reason I used a Hash Map data structure is because it allowed me to quickly access any key/value pair within the Double Ended Queue in constant time, O(1) with a space efficiency of O(n).