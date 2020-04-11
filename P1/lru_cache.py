'''
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

'''
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            raise ValueError("capacity must be a positive number")
        self.table = dict()
        self.capacity = capacity
        self.count = 0
        self.head = None
        self.tail = None

    def get(self, key):
        # if the key exists in the hash table, update the cache order and return the value. If not, return -1
        if key in self.table:
            node = self.table[key]
            if node == self.tail:
                return node.value
            self.remove(node)
            self.set_tail(node)
            return node.value
        else:
            return -1 

    def set(self, key, value):
        new_node = Node(key, value)

        # Set the value as a node if the key is not present in the cache.
        if key not in self.table:
            # If the cache is not at capacity, add the node to the hash_map and update the cache order
            if not self.count == self.capacity:
                self.set_tail(new_node)
                self.table[key] = new_node
                return
            # if the cache is at capacity, remove the node at the head from the linked list and hash map
            else:
                del self.table[self.head.key]
                self.remove(self.head)
                self.set_tail(new_node)
                self.table[key] = new_node
                return
        else:
            self.remove(new_node)
            self.set_tail(new_node)
    
    def remove(self, node):
        # if empty, return nothing
        if self.head is None:
            print("head is none")
            return
        self.count -= 1
        # if node is the head or tail
        if self.head == node:
            self.head = node.next
            node.next = node.prev
            return
        elif self.tail == node:
            self.tail = node.prev
            node.prev.next = node.next
        
        # if there is only one node
        if node.next is None and node.prev is None:
            print("removed only value {}".format(node.value))
            self.head = None
            self.tail = None
            return

        # if node is in the middle of the linked list
        print("removed {}".format(node.value))
        node.prev.next = node.next
        return

    def set_tail(self, node):
        self.count += 1
        #if the linked list is empty
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        # Add the node to the end of the linked list
        self.tail.next = node
        self.tail = node
        return

# Inputs
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(5, 5);
our_cache.set(6, 6)


# Test Cases
test_cases = [1, 2, 9, 3]
for i in test_cases:
    print("Input: {}".format(i))
our_cache.get(test_cases[0])       # returns 1
our_cache.get(test_cases[1])       # returns 2
our_cache.get(test_cases[2])      # returns -1 because 9 is not present in the cache
our_cache.get(test_cases[3])      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry