from collections import deque
from typing import *


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        self.dfs(node, cloned)
        return cloned[node]

    def dfs(self, node, cloned):
        if node in cloned:
            return
        cloned[node] = Node(node.val)
        for nei in node.neighbors:
            self.dfs(nei, cloned)
            cloned[node].neighbors.append(cloned[nei])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        self.bfs(node, cloned)
        return cloned[node]

    def bfs(self, node, cloned):
        queue = deque([])
        queue.append(node)
        cloned[node] = Node(node.val)
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    queue.append(nei)
                cloned[node].neighbors.append(cloned[nei])


if __name__ == '__main__':
    init = CloneGraph()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [one, three]
    print(init.cloneGraph(one))
