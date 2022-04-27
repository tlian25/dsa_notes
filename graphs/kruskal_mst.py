# Kruskal's Minimum Spanning Tree Algorithm
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
'''
Given a connected and undirected graph, 
a spanning tree of that graph is a subgraph that is 
a tree and connects all vertices together

A minimum spanning tree (MST) is one with a weight less
than or equal to every other spanning tree

High level algorithm

1. Sort all edges in non-decreasing order of weight
2. Pick smallest edge. check if it forms a cycle with spanning tree so far
3. If cycle is not formed, include edge, otherwise discard
4. Repeat 2-3 until there are V-1 edges in spanning tree
'''

from collections import defaultdict

class Graph:
    
    def __init__(self, vertices:int):
        self.V = vertices # No. of vertices 0 to vertices-1
        self.graph = []
        
    def addEdge(self, u:int, v:int, w:int):
        self.graph.append( (u, v, w) )
        
    # Find set of an element i
    # uses path compression technique
    def find(self, parent:int, i:int):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    # Takes union of two sets X and Y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

            

        
        
        