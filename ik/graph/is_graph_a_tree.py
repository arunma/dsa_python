from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1, 2


def is_it_a_tree(node_count, edge_start, edge_end):
    if node_count == 1 and not edge_start:
        return True

    if len(edge_start) != node_count - 1:
        return False
    graph = defaultdict(list)
    for u, v in zip(edge_start, edge_end):
        graph[u].append(v)
        graph[v].append(u)

    if len(graph) < node_count:
        return False

    colors = defaultdict(int)
    visited = set()
    for node in range(node_count):
        if has_cycle(node, graph, -1, colors, visited):
            return False

    return len(visited) == node_count


def has_cycle(node, graph, parent, colors, visited):
    visited.add(node)
    colors[node] = GRAY

    for nei in graph[node]:
        if colors[nei] == WHITE:
            if has_cycle(nei, graph, node, colors, visited):
                return True
        elif colors[nei] == GRAY and nei != parent:
            return True
        else:
            continue

    colors[node] = BLACK
    return False


if __name__ == '__main__':
    print(is_it_a_tree(node_count=4, edge_start=[0, 0, 0], edge_end=[1, 2, 3]))  # true
    print(is_it_a_tree(node_count=4, edge_start=[0, 0], edge_end=[1, 2]))  # false
    print(is_it_a_tree(node_count=4, edge_start=[0, 0, 0, 1], edge_end=[1, 2, 3, 0]))  # false
