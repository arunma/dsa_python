from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1, 2


def can_be_completed(n, a, b):
    graph = defaultdict(list)
    for u, v in zip(a, b):
        graph[u].append(v)

    print(graph)
    colors = defaultdict(int)
    for n in range(n):
        if colors[n] == WHITE:
            if has_cycle(n, graph, colors):
                return False
    return True


def has_cycle(n, graph, colors):
    colors[n] = GRAY
    for nei in graph[n]:
        if colors[nei] == WHITE:
            if has_cycle(nei, graph, colors):
                return True
        elif colors[nei] == GRAY:
            return True
        else:
            continue

    colors[n] = BLACK
    return False


if __name__ == '__main__':
    print(can_be_completed(4, [1, 1, 3], [0, 2, 1]))
