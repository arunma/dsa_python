def largest_connected_component(grid):
    R = len(grid)
    C = len(grid[0])

    max_count = float('-inf')
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                grid[r][c] = 1
                seen = set()
                count = [0]
                dfs(r, c, R, C, grid, seen, count)
                max_count = max(max_count, count[0])
                grid[r][c] = 0
    return max_count if max_count > float('-inf') else R * C


# def dfs(r, c, R, C, grid, seen):
#     seen.add((r, c))
#     neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
#     count = 0
#     for nr, nc in neis:
#         if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 1:
#             print(f"nr: {nr}, nc: {nc}")
#             count = 1 + dfs(nr, nc, R, C, grid, seen)
#     return count

def dfs(r, c, R, C, grid, seen, count):
    seen.add((r, c))
    count[0] += 1
    neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for nr, nc in neis:
        if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 1:
            # print(f"nr: {nr}, nc: {nc}")
            dfs(nr, nc, R, C, grid, seen, count)


if __name__ == '__main__':
    print(largest_connected_component(grid=[
        [1, 0],
        [0, 0]
    ]))  # 2

    print(largest_connected_component(grid=[
        [1, 1],
        [1, 1]
    ]))  # 4

    print(largest_connected_component(grid=[
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 1],
    ]))  # 7
