import hashlib
import datetime

def calc_hash(data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.utcnow()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.previous_block = None

class Blockchain:

    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data, previous_hash):
        if self.head is None:
            self.head = Block(data, 0)
            return
        self.count += 1
        new_block = Block(data, self.head.hash)
        new_block.previous_block = self.head
        self.head = new_block

    def size(self):
        if self.head is None:
            return 0
        return self.count
    
    def to_list(self):
        block_list = []
        block = self.head
        while block is not None:
            block_list.append(block)
            block = block.previous_block
        return block_list

# Test Cases
print("Test 1")
blockchain = Blockchain()
blockchain.append("First Value", None)
blockchain.append("Second Value", calc_hash("First Value"))
print(blockchain.to_list()) # Should return two nodes

print("Test 2")
test2 = Blockchain()
test2.append("AKLD", None)
blockchain.append(calc_hash("AKLD"), "ASFHKSLFGAKLGJKNGAKLNGAERGGLASJKHGALKRGAKLEG")
print("size", blockchain.size()) # Should return 2

print("Test 3")
empty = Blockchain()
print("size", empty.size()) # Should return 0
        
