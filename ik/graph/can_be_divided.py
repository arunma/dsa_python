from collections import defaultdict


def can_be_divided(num_of_people, dislike1, dislike2):
    graph = defaultdict(list)
    for u, v in zip(dislike1, dislike2):
        graph[u].append(v)
        graph[v].append(u)

    # print(graph)
    colors = {}
    for n in range(num_of_people):
        if n not in colors:
            colors[n] = 1
            if not is_two_colorable(n, colors, graph):
                return False
    return True


def is_two_colorable(n, colors, graph):
    for nei in graph[n]:
        if nei not in colors:
            colors[nei] = -colors[n]
            if not is_two_colorable(nei, colors, graph):
                return False
        elif colors[nei] == -colors[n]:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    print(can_be_divided(num_of_people=7, dislike1=[6, 6, 4, 4, 0], dislike2=[5, 3, 3, 5, 5]))
