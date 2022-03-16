# Single Source Shortest Path - Bellman Ford

# Works with negative edge weights
# Time complexity O(V*E)
# Min is O(n^2) and max is O(n^3) if complete graph

# Matrix representation


class Graph:
    def __init__(self, nodes, edges):
        
        self.adjList = {}
        self.nodes = nodes
        self.edges = edges
        
        for n in nodes:
            self.adjList[n] = []
            
        for (src, dest, weight) in edges:
            self.adjList[src].append( (dest, weight) )
            
            
            
def bellmanFord(graph:Graph, source:int):
    dist = {}
    # Initally set all distances to inft
    for n in graph.nodes:
        dist[n] = float('inf')
    
    # set source to self dist as 0
    dist[source] = 0
    
    # Loop through n-1 times
    # Need n-1 to ensure minimum distances (in the absence of negative cycles)
    for i in range(len(graph.nodes)-1):
        # Loop through all edges
        for src, dest, weight in graph.edges:
            # Relax edges
            dist[dest] = min(dist[dest], dist[src] + weight)
            
            
    # After n-1 loops, we run once more to check for negative weight cycles
    # Don't update dist, but if we can further relax, then we know there is a negative weight cycle
    for src, dest, weight in graph.edges:
        if dist[dest] > dist[src] + weight:
            print("Graph contains negative weight cycle")
            print()
            return None
        
    # print shortest paths 
    print(f"Shortest paths from {source}")
    for n in graph.nodes:
        print(f"{source} -> {n}: {dist[n]}")
    
    print()
    return None
            
    
    
    
    
    
        
                       
            
# Function to print adjacency list representation of a graph
def printGraph(graph:Graph):
    for src in graph.adjList:
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 


# Example 1
nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2, 6),
         (1, 3, 5),
         (1, 4, 5),
         (2, 5, -1),
         (3, 2, -2),
         (4, 3, -2), 
         (3, 5, 1),
         (4, 6, -1),
         (6, 7, 3),
         (5, 7, 3)
         ]


graph = Graph(nodes, edges)
print()
bellmanFord(graph, 1)


# Example 2
nodes = [1, 2, 3, 4]

edges = [(1, 2, 4),
         (1, 4, 5),
         (4, 3, 3),
         (3, 2, -10),
         (2, 4, 5)  # This edge causes a negative cycle
         ]


graph = Graph(nodes, edges)
print()
bellmanFord(graph, 1)


