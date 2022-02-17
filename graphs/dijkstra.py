# Dijkstra's Shortest Path Algorithm - With loop to find min 

# Will not always work if there is a negative path weights
# Time complexity O( (V+E) * logV) using a min heap

from collections import defaultdict


class Graph():
    def __init__(self, vertices:int):
        self.V = vertices
        self.graph = [[None for column in range(vertices)]
                      for row in range(vertices)]
        
    def printSolution(self, dist:dict):
        print("Vertex Distance From Source")
        for node in range(self.V):
            print(node, ":", dist[node])
            
            
    
    def minDistance(self, dist:dict, seen:set):
        m = float('inf')
        
        for v in range(self.V):
            if dist[v] < m and v not in seen:
                m = dist[v]
                next_closest_node = v
                
        return next_closest_node
    
    
    def dijkstra(self, src):
        
        dist = {v:float('inf') for v in range(self.V)}
        dist[src] = 0
        seen = set()
        
        for _ in range(self.V): # Loop #nodes times
            
            u = self.minDistance(dist, seen)
            seen.add(u) # lock

            for v in range(self.V):
                dist_uv = self.graph[u][v]
                if dist_uv != 0 and v not in seen:
                    dist[v] = min(dist[v], dist[u] + dist_uv)
                    
            
        self.printSolution(dist)
            
            
        
        
        
        



# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
    
g.dijkstra(0)