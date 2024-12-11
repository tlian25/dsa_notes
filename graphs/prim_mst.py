# Prim's Algorithm (minimum spanning tree)
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/


"""
1. Start with a spanning tree (not minimum)
2. Create a set mstSet that tracks verticies already included in MST
3. Assign key-value to all verticies in graph. Initialize all values as INF
4. Set first vertex value as 0 to start
5. While mstSet does not include all vertices
    a. pick vertex u not in mstSet and has min key-value
    b. add u to mstSet
    c. update key-value of all adjacent vertices of u

"""


class Graph:

    def __init__(self, vertices: int):
        self.V = vertices
        # Adjacency matrix representation
        self.graph = [[0 for c in range(vertices)] for r in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u][v] = self.graph[v][u] = w

    def printMST(self, parent) -> int:
        print("Edge \t Weight")
        totalweight = 0
        for i in range(self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")
            totalweight += self.graph[i][parent[i]]

        print(f"Total Weight: {totalweight}")
        return totalweight

    # Find min key-value over all nodes not yet in mstSet
    def minKey(self, values, mstSet):
        mn_val = float("inf")
        mn_node = None

        for v in range(self.V):
            if values[v] < mn_val and v not in mstSet:
                mn_val = values[v]
                mn_node = v

        return mn_node

    def primMST(self, start_node: int = 0):

        mstSet = set()

        # Initalize values to Inf
        values = {i: float("inf") for i in range(self.V)}
        # Set starting vertex value to 0
        values[start_node] = 0

        # To store MST representation
        parent = {i: None for i in range(self.V)}
        parent[start_node] = start_node  # set starting node to root as itself

        # Loop N times
        for _ in range(self.V):

            # Pick min distance vertex not yet processed
            u = self.minKey(values, mstSet)

            # Put min dist vertex in MST
            mstSet.add(u)

            # Update dist value for all adjustment vertices of u
            # only if new dist < curr dist and adj not in mstSet
            for v in range(self.V):

                if v not in mstSet and 0 < self.graph[u][v] < values[v]:
                    values[v] = self.graph[u][v]
                    parent[v] = u

        return self.printMST(parent)


def test_example1():
    print()
    print("Test Example 1")

    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

    for start_node in range(g.V):
        total_weight = g.primMST(start_node)
        assert total_weight == 16


def test_example2():
    print()
    print("Test Example 2")

    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(7, 8, 7)
    g.addEdge(7, 6, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 5, 14)
    g.addEdge(3, 4, 9)
    g.addEdge(4, 5, 10)

    for start_node in range(g.V):
        totalweight = g.primMST(start_node)
        assert totalweight == 41


if __name__ == "__main__":

    test_example1()
    test_example2()
