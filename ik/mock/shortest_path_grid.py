# given = [[INF, -1, 0, INF],
#          [INF, INF, INF, -1],
#          [INF, -1, INF, -1],
#          [0, -1, INF, INF]]
#
# 0 - Door
# -1 - Wall
# INF - Empty
# room
#
# Find
# shortest
# path
# to
# door
# from each room.
#
# output:
# [[3, -1, 0, 1],
#  [2, 2, 1, -1],
#  [1, -1, 2, -1],
#  [0, -1, 3, 4]]
# ]]
# start - 0, 2
# end - 3, 0
#
# diagonal: no
# undirected
# graph
#
# testcases:
# empty
# graph
# anything
# beyond
# grid is considered
# a
# wall(-1)
#
# no
# start
# all
# walls
# just
# one
# door


def find_shortest_path(grid):
    if not grid:
        return

    R = len(grid)
    C = len(grid[0])

    output = []
    for r in range(R):
        output.append([])
        for c in range(C):
            output[r].append[0]

    start = (-1, -1)
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                start = (r, c, 0)

    seen = set()
    queue = deque([start])

    while queue:
        r, c, dist = queue.popleft()

        seen.add((r, c))
        output[r][c] = dist

        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] != -1:
                queue.append((nr, nc, dist + 1))

    return output


def find_shortest_path(grid):
    if not grid:
        return grid

    R = len(grid)
    C = len(grid[0])

    start_list = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                start.append([r, c, 0])

    if not start:
        return grid

    queue = deque(start_list)

    while queue:
        r, c, dist = queue.popleft()

        seen.add((r, c))
        grid[r][c] = dist

        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == 'INF':
                queue.append((nr, nc, dist + 1))

    return grid
