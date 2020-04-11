class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def create_table(llist):
    if llist.head is None:
        return {}
    hash_map = {}   
    node = llist.head
    while node:
        if node.value in hash_map:
            hash_map[node.value] += 1
        else:
            hash_map[node.value] = 1
        node = node.next
    return hash_map

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
        return llist_2
    elif llist_2.head is None:
        return llist_1

    hash_map_1 = create_table(llist_1)
    hash_map_2 = create_table(llist_2)

    for key_1, val_1 in hash_map_1.items():
        if key_1 in hash_map_2:
            hash_map_2[key_1] = max(val_1, hash_map_2[key_1])
        else:
            hash_map_2[key_1] = val_1

    new_list = LinkedList()
    for key, val in hash_map_2.items():
        for i in range(val):
            new_list.append(key)

    return new_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
        return llist_2
    elif llist_2.head is None:
        return llist_1

    hash_map_1 = create_table(llist_1)
    hash_map_2 = create_table(llist_2)
    intersection_hash_map = {}

    for key_1, val_1 in hash_map_1.items():
        if key_1 in hash_map_2:
            intersection_hash_map[key_1] = min(val_1, hash_map_2[key_1])

    new_list = LinkedList()
    for key, val in intersection_hash_map.items():
        for i in range(val):
            new_list.append(key)

    return new_list
    



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # Should return (32 -> 1 -> 1 -> 2 -> 35 -> 4 -> 4 -> 6 -> 6 -> 65 -> 9 -> 11 -> 3 -> 3 -> 21 ->)
print (intersection(linked_list_1,linked_list_2)) # Should return (4 -> 21 -> 6 -> 6 ->)

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # Should return (1 -> 1 -> 2 -> 35 -> 4 -> 4 -> 6 -> 6 -> 65 -> 7 -> 8 -> 9 -> 11 -> 3 -> 3 -> 21 -> 23 ->)
print (intersection(linked_list_3,linked_list_4)) # Should return an empty list

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6)) # Should return an empty list
print (intersection(linked_list_5,linked_list_6)) # Should return an empty list

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1, 2, 3, 2 ,4]
element_2 = [1, 1, 1, 4, 6, 7]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8)) # Should return (1 -> 1 -> 1 -> 2 -> 2 -> 3 -> 4 -> 6 -> 7 ->)
print (intersection(linked_list_7,linked_list_8)) # Should return (1 -> 4 ->)