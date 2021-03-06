# reference = https://brilliant.org/wiki/hash-tables/
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Node:
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
    

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

#slots = [None] * MIN_CAPACITY

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * 10
        self.head = None
        self.ll = LinkedList()


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.slots)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.capacity/self.get_num_slots()
        return load_factor



    def fnv1(self, key):
        self.key = key
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        self.key = key
        
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        
        """
        # Your code here
        
        prime_number = 5381
        encoded = key.encode('utf-8')
        for c in encoded:
            prime_number = ((prime_number * 33) ^ c) % 0x100000000

        return prime_number


    def hash_index(self, key):
        self.key = key
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        self.key = key
        self.value = value

        i = self.hash_index(key)

        self.slots[i] = ll.insert_at_head_or_overwrite(key, value)

        return self.slots

    def delete(self, key):
        self.key = key
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        value = self.slots[i]

        self.slots[i] = ll.delete(value)

        return self.slots


    def get(self, key):
        self.key = key
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        value = self.slots[i]
        return value



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")