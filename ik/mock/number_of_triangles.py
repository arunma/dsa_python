'''

Given n nodes connected by undirected edges, return the number of triangles in the graph

Example
Input: [[0, 1], [1, 2], [2, 0]]
Output: 1

'''
from collections import defaultdict


# -1 - 0 - 1
# |
# \
# 2
#
# 0 - 1
#
# 0 - 1 - 3
# \ /
# 2
#
# 0 - 1 - 2 - 3
#
# 0 - 1 - 3
#
# result = [0]
#
# DFS - 0
#
# colors = WHITE, GRAY and BLACK
#
# node, start_node, colors, path_size
# 0, 0, 0 = GRAY, 1
# 1, 0, 1 = GRAY, 2
# 0, 0,
# if node == start_node and colors[nnode] == GRAY and path_size == 3, 3
# result[0] += 1
#
# 2, 0, 2 = GRAY
# 3, 1, 2 = GRAY
#
# Testcase:
#
# - null
# graph
# - positive
# - triangle
# more
# than
# 4
# nodes - filtered
# out
#
# WHITE, GRAY, BLACK = 0, 1, 2


# def count_triangles(edges):
#     result = [0]
#
#     graph = defaultdict(list)
#     nodes = set()
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
#         nodes.add(u)
#         nodes.add(v)
#
#     for node in nodes:
#         seen = set()
#         dfs(graph, node, node, [node], result, seen)
#
#     print("result: ", result)
#     return result[0] // 3
#
#
# def dfs(graph, node, start_node, path, result, seen):
#     if len(path) == 3 and start_node in path:
#         result[0] += 1
#         return
#
#     seen.add(node)
#     for nei in graph[node]:
#         if nei not in seen:
#             dfs(graph, nei, start_node, path + [nei], result, seen)


# def count_triangles(graph):
#     def dfs(node, current_path, visited):
#         nonlocal count
#         visited[node] = True
#         current_path.append(node)
#
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 dfs(neighbor, current_path, visited)
#             elif neighbor in current_path and len(current_path) == 3:
#                 # Triangle found
#                 count += 1
#
#         current_path.pop()
#         visited[node] = False
#
#     count = 0
#     n = len(graph)
#     visited = [False] * n
#
#     for node in range(n):
#         if not visited[node]:
#             dfs(node, [], visited)
#
#     return count

def count_triangles(edges):
    result = 0
    graph = defaultdict(list)
    nodes = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        nodes.add(u)
        nodes.add(v)

    for i in nodes:
        for j in graph[i]:
            if i != j:
                for k in graph[j]:
                    if j != k and i in graph[k]:
                        result += 1
    print(result)
    return result % 6


if __name__ == '__main__':
    print(count_triangles([[0, 1], [1, 2], [2, 0]]))
    print(count_triangles([]))
    print(count_triangles([[0, 1], [1, 2], [2, 0], [2, 3]]))
