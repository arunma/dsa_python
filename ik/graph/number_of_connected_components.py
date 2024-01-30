from collections import defaultdict


def number_of_connected_components(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    count = 0
    for node in range(n):
        if node not in seen:
            dfs(node, graph, seen)
            count += 1

    return count


def dfs(node, graph, seen):
    seen.add(node)

    for nei in graph[node]:
        if nei not in seen:
            dfs(nei, graph, seen)
