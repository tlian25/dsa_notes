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
            return i # parent is self, marking node as a root
        return self.find_parent(self.parent[i]) # recursively find root

    
    def union(self, parent_u, parent_v) -> None:
        # Join together by setting parent of one node to the other node
        # This effectively also joins u and v in the same component as no cycle was detected
        self.parent[parent_u] = parent_v

    
    def isCyclic(self) -> bool:

        for u in self.graph:
            for v in self.graph[u]:
                print(u, v, self.parent)
                parent_u = self.find_parent(u)
                parent_v = self.find_parent(v)

                if parent_u == parent_v: # share same root parent, so we have a cycle
                    return True
                else:
                    self.union(parent_u, parent_v) # Join so u and v have same parent thus marking as a connected component

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