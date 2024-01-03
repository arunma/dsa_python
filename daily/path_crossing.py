class PathCrossing:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0, 0)
        seen = {curr}

        for c in path:
            if c == 'N':
                curr = (curr[0] + 1, curr[1])
            elif c == 'E':
                curr = (curr[0], curr[1] + 1)
            elif c == 'S':
                curr = (curr[0] - 1, curr[1])
            elif c == 'W':
                curr = (curr[0], curr[1] - 1)

            if curr in seen:
                return True
            seen.add(curr)
        return False


if __name__ == '__main__':
    init = PathCrossing()
    print(init.isPathCrossing(path="NES"))  # false
    print(init.isPathCrossing(path="NESWW"))  # true
    print(init.isPathCrossing(path="NESWW"))  # true
    print(init.isPathCrossing(path="NNSWWEWSSESSWENNW"))  # true
