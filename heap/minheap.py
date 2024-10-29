# Implementation of Min Heap

'''
Notes: 
A min heap is a complete binary tree
typically represented as an array.
Arr[0] = root
Arr[i] = node i
Arr[ (i-1) // 2 ] = parent of node i
Arr[ (2*i) + 1 ] = left child of node i
Arr[ (2*i) + 2 ] = right child of node i

Operations:
getMin(): return root element, O(1) time complexity
extractMin(): pop root/min element from heap, O(logn) time complexity as we need to rebalance
insert(): insert next element, O(logn) time complexity to rebalance

'''

import sys

class MinHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        
        
    def parent(self, idx):
        return idx // 2
    
    def leftChild(self, idx):
        return 2 * idx
    
    def rightChild(self, idx):
        return 2 * idx + 1
    
    
    # Leaf node is furthest down so must be in second half of array
    # Array doubles with each level in tree/heap
    def isLeaf(self, idx):
        if idx > (self.size // 2) and idx <= self.size:
            return True
        return False
    
    def swap(self, pos1, pos2):
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]
        
        
    def minHeapify(self, idx):
        
        # Nothing to do if Leaf
        if self.isLeaf(idx): return None
        
        leftChildIdx = self.leftChild(idx)
        rightChildIdx = self.rightChild(idx)
        
        if (self.Heap[idx] > self.Heap[leftChildIdx] or
            self.Heap[idx] > self.Heap[rightChildIdx]):
            
            # Switch with smaller of left or right child
            if self.Heap[leftChildIdx] < self.Heap[rightChildIdx]:
                # Swap current and left child
                # Recursively rebalance down the heap
                self.swap(idx, leftChildIdx)
                self.minHeapify(leftChildIdx)
                
            else:
                # Swap current and right child
                # Recursively rebalance down the heap
                self.swap(idx, rightChildIdx)
                self.minHeapify(rightChildIdx)
                
    
    
    def insert(self, element):
        # Place new element in next empty spot
        # Recursively shift upward if smaller than parent
        if self.size >= self.maxsize:
            return # Or raise error
        
        self.size += 1
        self.Heap[self.size] = element # place in next empty spot on array
        
        current = self.size
        parent = self.parent(current)
        
        while self.Heap[current] < self.Heap[parent]:
            self.swap(current, parent)
            current = parent
            parent = self.parent(current)
            
            
    def minHeap(self):
        for idx in range(self.size//2, 0, -1):
            self.minHeapify(idx)
            
    
    def remove(self):
        
        # Pop off front element
        popped = self.Heap[self.FRONT]
        # Swap last element to front and remove front element
        self.Heap[self.FRONT], self.Heap[self.size] = self.Heap[self.size], None
        self.size -= 1
        # rebalance heap
        # Recursively swap with children if larger
        self.minHeapify(self.FRONT)
        return popped
    
    
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(f" IDX: {i} PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i + 1]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 2])
                  )
            
            
            
if __name__ == '__main__':
    
    minHeap = MinHeap(20)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
    
    while minHeap.size > 0:
        print('The minHeap is ')
        print(f'Size: {minHeap.size}')
        minHeap.Print()
        print("The Min val is " + str(minHeap.remove()))
        print()             
    
        