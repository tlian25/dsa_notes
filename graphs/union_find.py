# Disjoint Set / Union-Find
# https://www.geeksforgeeks.org/union-find/

'''
Detect Cycle in an Undirected Graph

1. Initialize a map of parents for each node set to itself
2. For each pair of nodes, check the root parent of each
    a. If roots are the same, the two nodes are already connected so joining them would cause a cycle
    b. If roots are not the same, we connect them by marking them to have the same root parent
3. Repeat step 2 until all edges have been examined. Break early if we hit case 2a


'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices:int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.parent = [i for i in range(self.V)] # initialize parent as self

    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def find_parent(self, i):
        if self.parent[i] == i:
            return i # parent is self
        return self.find_parent(self.parent[i]) # recursively find root

    
    def union(self, x, y) -> None:
        self.parent[x] = y

    
    def isCyclic(self) -> bool:

        for i in self.graph:
            for j in self.graph[i]:
                print(i, j, self.parent)
                x = self.find_parent(i)
                y = self.find_parent(j)

                if x == y: # share same root parent, so we have a cycle
                    return True
                else:
                    self.union(x, y) # Join so i and j have same parent thus marking as a connected component

        return False



def test_1():
    g = Graph(5)
    edges = [(0, 1), (1, 2), (2, 3), (4, 3), (0, 4)]
    for u, v in edges:
        g.addEdge(u, v)


    cycle = g.isCyclic()
    assert cycle == True


def test_2():
    g = Graph(5)
    edges = [(0, 1), (1, 2), (2, 3), (0, 4)]
    for u, v in edges:
        g.addEdge(u, v)


    cycle = g.isCyclic()
    assert cycle == False