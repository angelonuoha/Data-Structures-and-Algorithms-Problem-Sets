'''
Huffman Coding
'''

import sys
import heapq

class Huffman_Node(object):
    def __init__(self, value, wt):
        self.value = value
        self.wt = wt
        self.right = None
        self.left = None
    
    def __lt__(self, other):
        return self.wt < other.wt

def count_freq(data):
    hash_map = dict()
    # Save frequency of each letter in a hash map
    for ltr in data:
        if ltr in hash_map:
            hash_map[ltr] += 1
        else:
            hash_map[ltr] = 1

    # Create a sorted list of tuples: (frequency, value)
    sorted_freq = sorted(zip(hash_map.values(), hash_map.keys()))

    # Replace each tuple with a Huffman Node that uses the frequency as its weight
    for i in range(len(sorted_freq)):
        value = sorted_freq[i][1]
        wt = sorted_freq[i][0]
        sorted_freq[i] = Huffman_Node(value, wt)

    return sorted_freq

def htree(data):
    heap = count_freq(data)

    # Create heap data structure 
    heapq.heapify(heap)
    while len(heap) != 1:
        node = Huffman_Node(None, None)
        lft = heapq.heappop(heap)
        node.left  = lft
        rgt = heapq.heappop(heap)
        node.right  = rgt
        node.wt = lft.wt + rgt.wt
        heapq.heappush(heap, node)

    return heap

def htable(root):
    code_table = {}
    # Recursive function to add "0" to all left pointers in the table and "1" to all right pointers to create unique codes for each character
    def create_code(current_node, current_code = ""):
        if current_node is None:
            return
        if current_node.left is None and current_node.right is None:
            code_table[current_node.value] = current_code
        create_code(current_node.left, current_code + "0")
        create_code(current_node.right, current_code + "1")

    create_code(root[0])
    return code_table


def huffman_encoding(data):
    # Create an encoded string by replacing each character in the input string with the unique binary code created for each letter
    encoded = ""
    root = htree(data)
    table = htable(root)

    # If there is only one unique character in the input string
    if len(count_freq(data)) == 1:
        return "0" * len(data), root

    for char in data:
        encoded += table[char]
    
    return encoded, root

def huffman_decoding(data,tree):
    root = tree[0]
    if len(count_freq(data)) == 1:
        return len(data) * str(root.value)
    decoded_string = ""
    n = len(data)
    count = 0
    while count < n:
        current_node = root
        while current_node.left is not None and current_node.right is not None:
            if data[count] == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            count += 1
        decoded_string += current_node.value

    return decoded_string


def hoffman_test(data):
    if data is None:
        print(None)
        return
    if data == "":
        print("Please input a valid string\n")
        return
    print("Input: {}\n".format(data))

    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    
    encoded_data, tree = huffman_encoding(data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

# Test Cases
print("Test 1\n")
hoffman_test("The bird is the word")
print("Test 2\n")
hoffman_test("p")
print("Test 3\n")
hoffman_test("AAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCEEEEEEEEEEEEEKKKKKKKKKKKKKKDKDDJDJJDHDFWOFALHFSGJKAJKHFGKJRALGB")
print("Test 4\n")
hoffman_test("03")
