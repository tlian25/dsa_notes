class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size

        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        while self.group[node] != node:
            node = self.group[node]
        return node

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)

        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group2] = group1
            self.rank[group1] += 1

        return True


def test_1():
    g = UnionFind(5)
    edges = [(0, 1), (1, 2), (2, 3), (4, 3), (0, 4)]
    cycle = False
    for u, v in edges:
        if not g.join(u, v):
            cycle = True
            break

    assert cycle == True


def test_2():
    g = UnionFind(5)
    edges = [(0, 1), (1, 2), (2, 3), (0, 4)]
    cycle = False
    for u, v in edges:
        if not g.join(u, v):
            cycle = True
            break

    assert cycle == False


def test_3():
    g = UnionFind(9)
    edges = [(0, 1), (1, 2), (2, 3), (0, 4), (5, 6), (5, 7), (6, 8)]
    cycle = False
    for u, v in edges:
        if not g.join(u, v):
            cycle = True
            break

    print(g.group)
    print(g.rank)

    assert cycle == False
