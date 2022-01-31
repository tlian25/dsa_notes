# Practice with Kosoraju's Algorithm

from collections import defaultdict

class Graph:
    def __init__(self, nodes:list, edges:list):
        self.nodes = nodes
        self.edges = edges
        

nodes = [1,2,3,4,5,6,7,8,9]
edges = [(1,7), (4,1), (7, 4), (7,9), (3,9), 
         (9,6), (6,3), (6,8), (8,2), 
         (2,5), (5,8)]
        
g = Graph(nodes, edges)

def kosaraju(g:Graph):
    
    nodes = g.nodes
    
    edges = defaultdict(list)
    edgesrev = defaultdict(list)
    for e in g.edges:
        edges[e[0]].append(e[1])
        edgesrev[e[1]].append(e[0])
    
    # 1. DFS on graph with finishtime order
    finishorder = []
    # Global seen for DFS
    seen = set()
    def dfs1(n):
        if n not in seen:
            seen.add(n)
            for nb in edges[n]:
                dfs1(nb)
            finishorder.append(n)
                
    for n in nodes[::-1]:
        dfs1(n)
        
    print("Finish Order:", finishorder)
    
    # 2. DFS on reverse graph in finishtime stack order
    # Global seen for DFS
    seen = set()
    # Track SCC for each loop and return
    def dfs2(n, scc):
        if n not in seen:
            seen.add(n)
            scc.append(n)
            for nb in edgesrev[n]:
                scc = dfs2(nb, scc)
        return scc
            
    while finishorder:
        start = finishorder.pop()
        scc = dfs2(start, [])
        if scc:
            print("SSC from", start, scc)

        
    
    
kosaraju(g)
        
        
        
    
    