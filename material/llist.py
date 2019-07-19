# Week 3: Linked List
# Stack
# Queue-based questions


# ----------------------
# linked list
# ----------------------

# last time we did
# array
# [0, 1, 2, 3]
# loc = start + (index * offset)
# val = lookup(loc)

# {x}
# {x, next}

# x -> y -> z -> p
# |
# start
#
# normal insertion is O(1)
# a -> x -> y -> z -> p
# |
# start
#
# sorted insertion is not O(1)
# x -> y -> a -> z -> p
# |
# start

# double linked list
# x <-> y <-> z <-> p
# more memory, navigation is easier

# circular linked list
#  x -> y---- start
#  |    |
#  p <- z

# how to detect if it is circular?
"""
seen = set()
for node in linked_list:
    if node in seen:
        print("yeh toh circular hai!")
    seen.add(node)
"""
# pointers
# id(x)
"""
ghoda, gadha = 0, 0
while True:
    ghoda += 2
    gadha += 1
    if location(ghoda) == location(gadha):
        print("ye toh circular hai")
        break
"""
#  x -> y---- start
#  |    |
#  p <- z
# 0, 0  | y, y
# 2, 1  | p, z
# 0, 2  | y, p
# 2, 3  | p, x
# 0, 0  | y, y  - circular!


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
a.next = b

# adjacency matrix of a graph
#  a  b  c
# [0, 0, 1] a
# [0, 0, 0] b
# [0, 0, 0] c
# possible roads = n * n

# a <-> c
# sparse representations

# stack
# =========================================
#
eqn = ")1 + 2 + (3 + 4)("
eqn = "(1 + 2 + (3 + 4))"
# parenthesis balancing
print(eqn.count("(") == eqn.count(")"))
stack = []
for char in eqn:
    if char == ")":
        stack.pop()
    elif char == "(":
        stack.append("Seen an open bracked")
print(len(stack) == 0)
# reversal operations
stack = []
eqn = "arjoonn"
for char in eqn:
    stack.append(char)
while stack:
    print(stack.pop(), end="")
print("")
# https://en.wikipedia.org/wiki/Finite-state_machine
# pushdown automaton
#
# 1+2  infix notation
# +12  prefix / polish notation? shaayad
# 12+  postfix
import dis


def function(a, b):
    return a + b


# Python is a stack machine
# WASM is also a stack machine
# von neumann architecture (stack based architecture)


print(dis.dis(function))
# True
# True
# nnoojra
# 123           0 LOAD_FAST                0 (a)
#               2 LOAD_FAST                1 (b)
#               4 BINARY_ADD
#               6 RETURN_VALUE
# None

# queue
# ===================

queue = []
for i in range(10):
    queue.append(i)

while queue:
    print(queue.pop(), end=" ")
print("")

# lists are good for a lot of things. They start creating problems when:
lst = ["x"]
lst.index("x")  # O(n) use a dict O(1)
"x" in lst  # O(n)  use a set/dict O(1)
from collections import deque

ls = deque()
ls.append(10)
# priority queue
# heap

import heapq

# (x)---- y
#  |
#  +----- z
# minheap x <= y and x <= z
# maxheap x >= y and x >= z
# insert needs balacing the heap
# delete needs balacing the heap
# root is always min/max of item

heap = []
# [1, 1, 1, 1, 1, 1, 1]
#  0 |1  2 |3  4  5  6
# 0
# 1     2
# 3 4   5 6
# n -> 2n+1, 2n+2  children
# base structure + properties


# https://docs.python.org/3/library/heapq.html?highlight=heap#module-heapq
heap = []
heapq.heapify([])
print(heap)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
print(heap)

# heap sort

heap = []
n = 10
nos = list(range(n))
heap = nos[n // 2 :] + nos[: n // 2]
print(heap)
heapq.heapify(heap)
final = []
while heap:
    final.append(heap.pop(0))
    heapq.heapify(heap)
print(final)
# True
# True
# nnoojra
# 123           0 LOAD_FAST                0 (a)
#               2 LOAD_FAST                1 (b)
#               4 BINARY_ADD
#               6 RETURN_VALUE
# None
# 9 8 7 6 5 4 3 2 1 0
# []
# [1, 3, 2]
# [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# http://bigocheatsheet.com/
