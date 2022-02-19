# A* (start) algorithm
# 
# Small extension to Dijkstra that takes into account direction towards target
# Additional heuristic of how far left to go 
# 
# Same idea as dijkstra except we add edge weight and heuristic distance 
# for a total weight on heap. 
#
# Prioritize nodes going towards right direction of target

# Another way to think about it is with 3 costs
# G cost = distance from source, think travel distance
# H cost = distance from destination (heuristic), think distance left to go
# F cost = G + H = total cost (want to minimize), think minimum path between two points

from heapq import *
from collections import defaultdict

class Graph:
    def __init__(self, nodes, edges):
        
        self.nodes = nodes
        self.edges = edges
        self.weights = {}
        
        for n in nodes:
            self.weights[n] = defaultdict(int)
            
        for (src, dest, weight) in edges:
            self.weights[src][dest] = weight
            self.weights[dest][src] = weight
            
            
def aStar(graph:Graph, source:str, dest:str, heurdist:dict):
    
    processed = set()
    path_order = []
    
    dist = {v:float('inf') for v in graph.nodes}
    dist[source] = 0
    
    # Start with source
    totalWeight = graph.weights[source][dest] + heurdist[source]
    heap = [(totalWeight, source)]
    
    while heap:
        
        tw, curr = heappop(heap)
        processed.add(curr)
        path_order.append(curr)

        if curr == dest:
            print(f"Path found: {path_order}")
            print()
            return None
        
        heap = []
        
        for nb in graph.nodes:
            if nb not in processed and graph.weights[curr][nb] > 0:
                # Relax edge
                dist[nb] = min(dist[nb], dist[curr] + graph.weights[curr][nb])
                # Add edge weight dist and heuristic distance (heuristic)
                w = dist[nb] + heurdist[nb]
                heappush(heap, (w, nb))
                
    
    print(f"Path not found. Processed {processed}. Path Order: {path_order}")
    print()
    return None
    
    
    
            
            
            
# Example 1    
# s = start
# e = end
nodes = ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l']

# Edges - source, dest, weight
edges = [('s', 'a', 7),
         ('s', 'b', 2),
         ('s', 'c', 3),
         ('b', 'd', 6),
         ('b', 'h', 1),
         ('b', 'd', 4),
         ('d', 'f', 5),
         ('h', 'f', 3),
         ('h', 'g', 2),
         ('g', 'e', 2),
         ('e', 'k', 5),
         ('k', 'i', 4),
         ('j', 'k', 4),
         ('i', 'j', 6),
         ('i', 'l', 4),
         ('j', 'l', 4),
         ('l', 'c', 2)]

# Heuristic - euclidian distance from DEST ('e')
heurdist = {'s': 10, 
                'a': 9,
                'b': 7,
                'c': 8,
                'd': 8,
                'e': 0,
                'f': 6,
                'g': 3,
                'h': 6,
                'i': 4,
                'j': 4,
                'k': 3,
                'l': 6}

graph = Graph(nodes, edges)

print()
aStar(graph, 's', 'e', heurdist)
