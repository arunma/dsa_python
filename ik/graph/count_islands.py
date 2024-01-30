def count_islands(grid):
    if not grid:
        return 0
    islands = 0
    R = len(grid)
    C = len(grid[0])

    seen = set()
    for r in range(R):
        for c in range(C):
            if (r, c) not in seen and grid[r][c] == 1:
                seen.add((r, c))
                dfs(r, c, R, C, grid, seen)
                islands += 1
    return islands


def dfs(r, c, R, C, grid, seen):
    neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1), ]
    for nr, nc in neis:
        if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 1:
            seen.add((nr, nc))
            dfs(nr, nc, R, C, grid, seen)


if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    print(count_islands(grid))  # 5
