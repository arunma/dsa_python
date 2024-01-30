from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1, 2


def find_order(words):
    graph = defaultdict(list)
    for word1, word2 in zip(words, words[1:]):
        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                continue
            else:
                graph[c1].append(c2)
                break

    colors = defaultdict(int)
    result = []
    all_nodes = [c for word in words for c in word]
    for node in set(all_nodes):
        if colors[node] == WHITE:
            if has_cycle(node, graph, colors, result):
                return ""

    return ''.join(reversed(result))


def has_cycle(node, graph, colors, result):
    colors[node] = GRAY
    for nei in graph[node]:
        if colors[nei] == GRAY:
            return True
        elif colors[nei] == WHITE:
            if has_cycle(nei, graph, colors, result):
                return True
        else:
            continue
    colors[node] = BLACK
    result.append(node)
    return False


if __name__ == '__main__':
    # print(find_order(["baa", "abcd", "abca", "cab", "cad"]))  # bdac
    # print(find_order(["caa", "aaa", "aab"]))  # cab
    print(find_order(["g", "g", "g"]))  # g
