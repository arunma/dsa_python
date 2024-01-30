class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"{self.value}: {self.neighbors}"

    def __repr__(self):
        return f"{self.value}: {self.neighbors}"


def create_transpose(node):
    transposed = {}
    dfs(transposed, node)
    return transposed[node]


# def dfs(transposed, node, seen):
#     seen.add(node)
#     if node not in transposed:
#         transposed[node] = GraphNode(node.value)
#     for nei in node.neighbors:
#         if nei not in seen:
#             dfs(transposed, nei, seen)
#         if nei not in transposed:
#             transposed[nei] = GraphNode(nei.value)
#
#         transposed[nei].neighbors.append(transposed[node])


def dfs(transposed, node):
    if node in transposed:
        return
    transposed[node] = GraphNode(node.value)
    for nei in node.neighbors:
        dfs(transposed, nei)
        transposed[nei].neighbors.append(transposed[node])


#
# def dfs(transposed, node, seen):
#     seen.add(node)
#     # if node not in transposed:
#     transposed[node] = GraphNode(node.value)
#     for nei in node.neighbors:
#         if nei not in seen:
#             dfs(transposed, nei, seen)
#         # if nei not in transposed:
#         transposed[nei] = GraphNode(nei.value)
#
#         transposed[nei].neighbors.append(transposed[node])


if __name__ == '__main__':
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node1.neighbors.append(node2)
    node2.neighbors.append(node3)
    node3.neighbors.append(node1)

    print(create_transpose(node1))
