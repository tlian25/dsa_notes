# Graph representation of A*
# https://www.annytab.com/a-star-search-algorithm-in-python/


class Node:

    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # distance to start node
        self.h = 0  # distance to end node
        self.f = 0  # total cost

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"({self.name}, {self.f})"


class Graph:
    def __init__(self, graph_dict={}, directed=True):
        self.graph_dict = graph_dict
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in self.graph_dict:
            for b, dist in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
