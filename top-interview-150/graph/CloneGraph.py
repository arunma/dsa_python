from collections import deque
from typing import *


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        store = {node: Node(node.val)}

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in store:
                    store[nei] = Node(nei.val)
                    queue.append(nei)

                store[curr].neighbors.append(store[nei])
        return store[node]


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
