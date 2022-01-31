from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        self.stack = []
        
    def add_edge(self, s, d):
        self.graph[s].append(d)
        
        
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[d]:
                self.dfs(i, visited_vertex)
                
    def fill_order(self, d, visited_vertex):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex) 
        self.stack.append(d)
        
        
    # reverse graph edges
    def transpose(self):
        g = Graph(self.V)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    
    
    def print_scc(self):
        visited_vertex = [False] * (self.V)
        
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex)
                
        # Reverse graph
        visited_vertex = [False] * (self.V)

        gr = self.transpose()
        print(self.stack)
        while self.stack:
            i = self.stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")
                
                
        
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
            
        
        