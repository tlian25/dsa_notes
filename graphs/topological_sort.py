# Topological Sort

# DFS approach with temporary stack

from collections import defaultdict

class Graph:
    def __init__(self, vertices:int):
        self.graph = defaultdict(set)
        self.V = vertices
        self.visited = {}
        self.stack = []
        self.rank = {}
        
    def addEdge(self, u, v):
        self.graph[u].add(v)
        
    
    # Recursive DFS function
    def dfs(self, v:int) -> None:
        
        # Mark current node as visited
        self.visited[v] = True
        
        # Recurse for all adjacent vertices
        
        for nb in self.graph[v]:
            if self.visited[nb] == False:
                self.dfs(nb)
                
                
        # Push current vertex to stack which stores result in finish order
        self.stack.append(v)
        
        
    # Topological sort
    def topologicalSort(self):
        
        self.visited = {i:False for i in range(self.V)}
        self.stack = []
        
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs(i)
                
        self.stack = self.stack[::-1] 
        return self.stack
    
    
    # Ranking
    def dfsRank(self, v:int) -> int:
        if v in self.rank:
            return self.rank[v] + 1
        
        r = 0
        for nb in self.graph[v]:
            r = max(r, self.dfsRank(nb))
            
        self.rank[v] = r
        return r + 1
    
    # Rank Sorting - Rank == Number of children
    def rankSort(self):
        
        for i in range(self.V):
            self.dfsRank(i)
        
        
        return [x[0] for x in sorted(self.rank.items(), key = lambda x: x[1], reverse=True)]
            
        
        


def test_1():
    
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    ts = g.topologicalSort()
    rs = g.rankSort()
    print('Topological Sort', ts)
    print('Rank Sort', rs)
    
test_1()
        
        
        
def test_2():
    g = Graph(8)
    for e in [(0,1), (0,2), (1,7), (1,4), (0,4), (0,3), (2,3), (4,5), (4,6)]:
        g.addEdge(e[0], e[1])
        
    ts = g.topologicalSort()
    rs = g.rankSort()
    print('Topological Sort', ts)
    print('Rank Sort', rs)
    
test_2()
    
    
def test_3():
    g = Graph(6)
    for e in [(0,1), (0,5), (1,2), (1,3), (2, 3), (2,4), (3, 5)]:
        g.addEdge(e[0], e[1])
        
    ts = g.topologicalSort()
    rs = g.rankSort()
    print('Topological Sort', ts)
    print('Rank Sort', rs)
    
test_3()