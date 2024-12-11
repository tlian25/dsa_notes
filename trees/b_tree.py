# B-Tree
"""
Nodes hold more than 1 key
Each node has 1 more children than # of keys

Rules:
1. The leaves of b-tree must all be on the same level of the tree. This ensure balance.
2. Every node has max and min number of keys. We determine max, and min is half of max.
3. Root node is exception and can have fewer than min keys
4. Every time we add a node, we start with root
5. When a node has > max keys, then we split, pushing middle element up and splitting into two children with (max-1) / 2 keys each
"""
from typing import List


class Node:
    def __init__(self, n: int = 4, isleaf: bool = True):
        self.keys = []
        self.children = []
        self.isleaf = isleaf

    def __str__(self):
        return f"Node={self.keys}"


class BTree:
    def __init__(self, n: int = 4):
        self.root = Node(self.n)
        self.n = n

    def find(self, num) -> bool:
        return False

    def insert(self, num) -> None:
        root = self.root
        if len(root.keys) > self.n:
            tmp = Node(self.n)

    def remove(self, num) -> None:
        pass

    def __str__(self):
        pass
