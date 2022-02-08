
import heapq

# Dijkstra with Priority Queue

class Graph():
    def __init__(self, vertices:int):
        self.V = vertices
        self.graph = [[None for column in range(vertices)]
                      for row in range(vertices)]
        
        self.dist = {v:float('inf') for v in range(self.V)}
        
    def printSolution(self):
        print("Vertex Distance From Source")
        for node in range(self.V):
            print(node, ":", self.dist[node])
            
    def relax(self, u:int, v:int):
        
        self.dist[v] = min(self.dist[v], self.dist[u] + self.graph[u][v])
    
    
    def dijkstra(self, src:int):
        
        self.dist[src] = 0
        processed = set()
        
        h = [] # heap
        heapq.heappush(h, (self.dist[src], src))
        
        while h:            
            d, u = heapq.heappop(h)
            processed.add(u)            
            h = []            
            for v in range(self.V):
                # Not yet processed and connected to current source u
                if v not in processed and self.graph[u][v] > 0: 
                    self.relax(u, v)
                    heapq.heappush(h, (self.dist[v], v))
                
        self.printSolution()
                
        



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