from collections import defaultdict


class PaintFence:

    # Wrong
    def numWays(self, n: int, k: int) -> int:
        return self.num_ways_inner(n, k, defaultdict(int))

    def num_ways_inner(self, n, k, counts):
        if n < 0:
            return 0
        if n == 0:
            return 1
        num_ways = 0
        for kk in range(k):
            if counts[kk] < 2:
                counts[kk] += 1
                num_ways += self.num_ways_inner(n - 1, k, counts)
                counts[kk] -= 1
        return num_ways % (10 ** 9 + 7)

    # Plain
    def numWays(self, n: int, k: int) -> int:
        return self.num_ways_inner(n, k, None, None)

    def num_ways_inner(self, n, k, prev, prevprev):
        if n < 0:
            return 0
        if n == 0:
            return 1
        num_ways = 0
        for color in range(k):
            if color == prev and color == prevprev:
                continue
            num_ways += self.num_ways_inner(n - 1, k, color, prev)
        return num_ways % (10 ** 9 + 7)

    # Memo - TLE
    def numWays(self, n: int, k: int) -> int:
        return self.num_ways_inner(n, 0, k, None, None, {})

    def num_ways_inner(self, n, i, k, prev, prevprev, memo):
        if (i, prev, prevprev) in memo:
            return memo[(i, prev, prevprev)]
        if n == i:
            return 1

        num_ways = 0
        for color in range(k):
            if color == prev and color == prevprev:
                continue
            num_ways += self.num_ways_inner(n, i + 1, k, color, prev, memo) % (10 ** 9 + 7)
        memo[(i, prev, prevprev)] = num_ways
        return num_ways

    # Memo - State variable reduction - Works
    def numWays(self, n: int, k: int) -> int:
        return self.num_ways_inner(n, k, None, False, {})

    def num_ways_inner(self, n, k, prev, last_two_same, memo):
        if (n, last_two_same) in memo:
            return memo[(n, last_two_same)]

        if n == 0:
            return 1

        total_ways = 0
        for color in range(k):
            if color == prev and last_two_same:
                continue
            total_ways += self.num_ways_inner(n - 1, k, color, color == prev, memo) % (10 ** 9 + 7)

        memo[(n, last_two_same)] = total_ways
        return total_ways


if __name__ == '__main__':
    init = PaintFence()
    print(init.numWays(n=3, k=2))  # 6
    print(init.numWays(n=1, k=1))  # 1
    print(init.numWays(n=7, k=2))  # 42
    print(init.numWays(n=2, k=46340))  #
