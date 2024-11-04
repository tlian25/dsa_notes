# Manual implementation of minimum heap
# Complete binary tree
# Parent is less than children nodes

from random import randint

class MinHeap:
    def __init__(self):
        self.h = [float('-inf')]

    def push(self, val) -> None:
        # add to last element in list and bubble up
        self.h.append(val)
        idx = len(self.h)-1
        parentidx = self.parentIdx(idx)
        while self.h[idx] < self.h[parentidx]:
            self.swap(idx, parentidx)
            idx = parentidx
            parentidx = self.parentIdx(idx)

    def pop(self) -> int:
        # swap with last element and pop off
        self.swap(1, len(self.h)-1)
        retval = self.h.pop()
        self.pushdown(1)
        return retval
    
    
    def pushdown(self, idx):
        leftidx = self.leftChildIdx(idx)
        rightidx = self.rightChildIdx(idx)

        greaterthanleft = bool(leftidx < len(self.h) and self.h[idx] > self.h[leftidx])
        greaterthanright = bool(rightidx < len(self.h) and self.h[idx] > self.h[rightidx])

        if greaterthanleft and greaterthanright:
            if self.h[leftidx] < self.h[rightidx]:
                self.swap(idx, leftidx)
                self.pushdown(leftidx)
            else:
                self.swap(idx, rightidx)
                self.pushdown(rightidx)
        elif greaterthanleft:
            self.swap(idx, leftidx)
            self.pushdown(leftidx)
        elif greaterthanright:
            self.swap(idx, rightidx)
            self.pushdown(rightidx)


    def leftChildIdx(self, idx) -> int:
        return idx * 2


    def rightChildIdx(self, idx) -> int:
        return idx * 2 + 1

    def parentIdx(self, idx) -> int:
        return (idx) // 2

    def isLeaf(self, idx) -> bool:
        return idx > len(self.h) // 2

    def swap(self, i, j) -> None:
        self.h[i], self.h[j] = self.h[j], self.h[i]
    
    def __repr__(self):
        return f'{self.h}'


def test1():
    h = MinHeap()
    h.push(100)
    h.push(200)
    h.push(150)
    h.push(50)
    assert h.pop() == 50
    assert h.pop() == 100

    h.push(75)
    h.push(50)
    h.push(50)
    h.push(100)
    assert h.pop() == 50 
    assert h.pop() == 50 
    assert h.pop() == 75


def test2():

    nums = [randint(1, 1000) for _ in range(1000)]

    h = MinHeap()
    for n in nums:
        h.push(n)
    
    for n in sorted(nums):
        assert h.pop() == n
    