import bisect
from cgi import test
import hashlib
import random
import numpy
from collections import defaultdict


# Arbitrary node class to represent a host or client
# e.g. Redis DB Client, Distributed Cache, etc.
class Node:
    def __init__(self):
        pass


class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self._replicas = replicas
        self._keys = []
        self._nodes = {}

    def _hash(self, key: str) -> str:
        """Given a string key, return a hash value."""
        return hashlib.md5(key.encode("utf-8")).hexdigest()

    def _repl_iterator(self, nodename) -> tuple:
        """Given a node name, return an iterable of replica hashes."""
        return (self._hash(f"{nodename}:{i}") for i in range(self._replicas))

    def __setitem__(self, nodename: str, node: Node) -> None:
        """
        Add a node, given its name.
        The given nodename is hashed among number of replicas.
        """

        for hash_ in self._repl_iterator(nodename):
            if hash_ in self._nodes:
                raise ValueError(f"Node name {nodename} already present")

            self._nodes[hash_] = node
            bisect.insort(self._keys, hash_)

    def __delitem__(self, nodename: str) -> None:
        """Remove a node, given its name."""
        for hash_ in self._repl_iterator(nodename):
            del self._nodes[hash_]
            idx = bisect.bisect_left(self._keys, hash_)
            del self._keys[idx]

    def __getitem__(self, key: str) -> Node:
        """Return a node, given a key.

        The node replica with a hash value nearest but not
        less than that of the given name is returned.
        If the hash of the given name is greater than the
        greatest has, returns the lowest hashed node.
        """

        hash_ = self._hash(key)
        start = bisect.bisect(self._keys, hash_)
        if start == len(self._keys):  # If greater than end, wrap around
            start = 0
        return self._nodes[self._keys[start]]


def _pop_std_dev(population) -> float:
    stddev = numpy.std(list(population.values()))
    return stddev


def test_get_distribution():
    ring = ConsistentHashRing(100)

    numnodes = 10
    numhits = 1000
    numvalues = 10000

    # Insert nodes
    for i in range(1, numnodes + 1):
        ring[f"node{i}"] = f"node_value_{i}"

    distributions = defaultdict(int)
    for i in range(numhits):
        key = str(random.randint(1, numvalues))
        node = ring[key]
        distributions[node] += 1

    for k, v in ring._nodes.items():
        print(k, v)

    for i, k in enumerate(ring._keys):
        print(i, k)

    # Assertions
    assert len(distributions) == numnodes
    assert sum(distributions.values()) == numhits
    keys = set(distributions.keys())
    assert keys == set(f"node_value_{i}" for i in range(1, numnodes + 1))

    standard_dev = _pop_std_dev(distributions)
    assert standard_dev <= 20


test_get_distribution()
