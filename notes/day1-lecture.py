# Hash Tables Live Coding Demo

def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff
    return total

my_array = [None] * 8
print(f'my_array {my_array}')

# Storing a value
hash_index = my_hash("hello world") % 8
print(f'hash_index {hash_index}')

my_array[hash_index] = 'my value'
print(f'my_array {my_array}')

# Get a value
hash_index = my_hash("hello world") % 8
print(my_array[hash_index])

# Deleting a value
hash_index = my_hash("hello world") % 8
my_array[hash_index] = None
print(my_array)

# Jewels and Stones

def numJewelsInStones(self, J: str, S: str) -> int:
    j = set(list(J))
    numJewels = 0
    for s in S:
        numJewels += 1 if s in j else 0
    return numJewels
