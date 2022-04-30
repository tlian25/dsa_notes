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
    def union(self, parent, rank, parent_u, parent_v):

        # Attach smaller rank tree under root of higher rank tree
        # Union by Rank
        if rank[parent_u] < rank[parent_v]:
            parent[parent_u] = parent_v
        elif rank[parent_v] < rank[parent_u]:
            parent[parent_v] = parent_u

        # If ranks are the same, then arbitrarily make one root of other
        # Increment its rank by one
        else:
            parent[parent_u] = parent_v
            rank[parent_u] += 1

            
    def kruskalmst(self):

        mst = [] # to hold edges in MST
        
        edge_idx = 0 # index 
        num_edges = 0 # Number of edges

        # sort all edges in non-decreasing order of their weight
        # create a copy if we are not allowed to change the given graph
        # graph = list of (u, v, w) edges
        self.graph = sorted(self.graph, key = lambda x: x[2])

        parent = []

        # Create V subsets with single elements
        parent = [node for node in range(self.V)]
        rank = [0 for node in range(self.V)]

        # number of edges taken equal to V-1 to create spanning tree
        while num_edges < self.V - 1:

            # pick smallest edge and increment index for next iteration
            u, v, w = self.graph[edge_idx]
            edge_idx += 1

            parent_u = self.find(parent, u)
            parent_v = self.find(parent, v)

            # If parents not the same, then we don't have a cycle and can join
            if parent_u != parent_v:
                num_edges += 1
                self.union(parent, rank, parent_u, parent_v)
                mst.append( (u,v,w) )
            
            # Else Do not include edge as it would cause a cycle
        
        print ("Edges in the constructed MST")
        minimumCost = 0
        for u, v, weight in mst:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)





# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
 
# Function call
g.kruskalmst()


        
        
        