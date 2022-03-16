# Bellman-Ford Graph Algorithm
# Find single-source shortest path
# Able to handle negative edge weights

# Reference: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = set()
        
        # Nested dictionary representation of graph
        self.graph = defaultdict(dict)
        
        
    # u -> v with w weight
    def addEdge(self, u, v, w):
        self.V.add(u)
        self.V.add(v)
        self.graph[u][v] = w
        
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in self.V:
            print(f"Node {i}:\t\t{dist[i]}")
            
    
    def BellmanFord(self, src):
        
        # Step 1: Initialize distances from src to INF
        dist = {i: float('inf') for i in self.V}
        dist[src] = 0
        
        # Step 2: Relax all edges |V|-1 times.
        # A simple shortest path from src to any node can have at-most |V|-1 edges
        for _ in range(len(self.V)-1):
            for u in self.graph:
                for v in self.graph[u]:
                    w = self.graph[u][v]                    
                    # If u reached from src, then look at path through u to v
                    # Relax if applicable
                    dist[v] = min(dist[v], dist[u] + w)
            
        # Step 3: Cycle through one more time to detect negative weight cycles
        # If we find any further relaxtion, then we have a negative weight cycle
        for u in self.graph:
            for v in self.graph[u]:
                w = self.graph[u][v]
                if dist[v] > dist[u] + w: # able to relax further
                    raise ValueError("Graph cntains negative weight cycle")
        
        self.printArr(dist)
    
    
# Example
g = Graph()
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
# Print the solution
g.BellmanFord(0)      
    
                            
            
        