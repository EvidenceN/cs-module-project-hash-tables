# CSPT10 Hash Tables II

hash_table = [None] * 8   # 8 slots, all initiailized to None

def my_hash(s):
    sb = s.encode()  # Get the UTF-8 bytes for the string

    total = 0

    for b in sb:
        total += b
        total &= 0xffffffff  # clamp to 32 bits

    return total

def hash_index(key):
    h = my_hash(key)
    return h % len(hash_table)

def put(key, val):
    i = hash_index(key)
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}!")
    hash_table[i] = val

def get(key):
    i = hash_index(key)
    return hash_table[i]

def delete(key):
    i = hash_index(key)
    hash_table[i] = None

put("Hello", "Hello Value")
put("World", "World Value")
put("foo", "foo value")   # "foo" hashes to same index as "Hello"
                          # AKA "foo collides with Hello"

print(hash_table)

lass Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

    # Runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Runtime O(number of nodes)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    # Runtime: O(number of nodes)
    # Space: O(1)
    def delete(self, value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            return curr

        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    # Runtime: O(number of nodes)
    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
ll.insert_at_head_or_overwrite(a)
print(ll)
