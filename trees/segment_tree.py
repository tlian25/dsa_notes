# Segment Tree
"""
Used for range queries such as sum, min, max
Tree is build recursively by dividing the array into segments until each segment represents a single element

Types of Operations
* Finding range sum queries
* Search index with given prefix sum
* Finding range max/min
* Counting frequency of range max/min

"""
from random import randint

# Method 1: Use an array to act as a segment tree


class SegTreeArray:
    def __init__(self, original_array):
        self.array = [None for _ in original_array] + [
            (n, i, i) for i, n in enumerate(original_array)
        ]

        for i in range(len(original_array) - 1, 0, -1):
            n1, l1, r1 = self.array[i * 2]
            n2, l2, r2 = self.array[i * 2 + 1]
            self.array[i] = (max(n1, n2), min(l1, l2), max(r1, r2))

    def query(self, l, r):
        mx = -1

        node = 1
        # Search down right index

    def __str__(self):
        return str(self.array)


class Node:
    def __init__(self, m, l, r):
        self.m = m
        self.range = [l, r]
        self.left = None
        self.right = None

    def values(self):
        return self.m, self.range[0], self.range[1]

    def __str__(self):
        return f"Node={self.m} {self.range}"


class SegTree:
    def __init__(self, array):
        self.array = [None for _ in array] + [
            Node(n, i, i) for i, n in enumerate(array)
        ]

        for i in range(len(array) - 1, 0, -1):
            n1, l1, r1 = self.array[i * 2].values()
            n2, l2, r2 = self.array[i * 2 + 1].values()
            self.array[i] = Node(max(n1, n2), min(l1, l2), max(r1, r2))
            self.array[i].left = self.array[i * 2]
            self.array[i].right = self.array[i * 2 + 1]

    def query(self, left, right):
        pass

    def __str__(self):
        return str([str(n) for n in self.array])


def run1():
    array = [randint(0, 100) for _ in range(10)]
    print(array)
    segTree = SegTree(array)
    print(segTree)

    print()
    segTree.query(2, 5)

    for node in segTree.array[1:]:
        print(node)
        print(node.left)
        print(node.right)
        print()


if __name__ == "__main__":
    run1()
