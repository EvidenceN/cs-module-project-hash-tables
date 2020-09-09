### Hash tables slides
https://docs.google.com/presentation/d/1G6ZmD0H5Yi_7emrP3zduOpAfDMaIRTLMZWI99qJD90o/edit#slide=id.g823334e007_0_390

### Hash tables example code snippets
https://hackmd.io/@sIQnCbQ0T56A3KLAiNrlhQ/Sy4woFh7v

### Implementing DJB2 in Python
https://hackmd.io/@sIQnCbQ0T56A3KLAiNrlhQ/r1GtXjBVP

## Hash functions

* Takes an input string and returns an index/number

### Main characteristics:

* *Deterministic* - same input should always result in the same output
* *Minimal duplication of output values* - to minimize collisions
* *fast* - getting the hash must be 0(1)


## Hash function in has tables
* A hash table uses a hash function to get/store/delete values in 0(1) time
* A hash table uses a list to store values
* Run the input string/key through the hash function
* Use the modulo operator to get an index within the array bounds
* Get/store/delte the value at that index

## Why it's called a hash function?

* To hash means to **chop something up or to make a mess out of it;**
the idea in hashing is to **scramble** some aspects of the key and to use this partial information
 as the basis for searching
* We are **scrambling** the input string and turning it into a number
* we use that number to get/store/delete values in the hash table

# Hash Collisions

## COLLISION RESOLUTION VIA CHAINING
* To solve collisions, chain values together by using linked lists
* If a value already exists at that index, add the new item to end of the linked list
* Operations of a hash table get slower if there are a lot of collisions

# LINKED LIST REVIEW
* Comprised of nodes
* Nodes contain: value, next pointer, previous (if doubly linked-list)
* To fully implement a hash table, we’re combining three things: hashing, arrays, linked lists

# Load Factor & Resizing
* The performance of a hash table worsens as there are more collisions
* To prevent this from happening, we need to know when to increase the size of our table
* Use load factor to determine when to expand/shrink
* Load factor = num elements / num slots
    * Expand table if load factor > 0.7
    * Shrink if < 0.2

# Hash Tables & Interviews

* There’s many use-cases for hash-tables in programming problems
* Hash-and-store: Use O(1) get/store/delete operations in dictionaries/sets to solve the problem faster, at the expense of additional space

# Collision Resolution Via Linear Probing
* Keys are stored in the table, instead of storing them in a linked list
* Size of table is >= number of keys
* If a collision occurs, walk the table until you find a free spot
* Tombstone an element when it’s deleted

# CHAINING VS. LINEAR PROBING

* Linear Probing has the following benefits:
*   * Low memory overhead - just need an array and a hash function
*   * Excellent caching performance - by taking advantage of arrays and cache locality
* Linear Probing has the following drawbacks:
*   * Gets very slow as load factor approaches 1 (why do you think that is?)
*   * You can never have more elements than the size of your array
* For the guided project you should use chaining as the collision resolution method

