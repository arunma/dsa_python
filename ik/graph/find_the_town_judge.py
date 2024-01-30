from collections import defaultdict


def find_town_judge(n, trust):
    graph = defaultdict(set)
    for u, v in trust:
        graph[u].add(v)

    judge = 1
    for cand in range(1, n + 1):
        if cand in graph[judge]:
            judge = cand

    if graph[judge]:
        return -1

    return judge


if __name__ == '__main__':
    print(find_town_judge(n=4, trust=[
        [1, 4],
        [2, 4],
        [3, 4]
    ]))  # 4
