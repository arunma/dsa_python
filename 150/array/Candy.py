from typing import *


class Candy:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N
        # l->r
        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == '__main__':
    init = Candy()
    print(init.candy([1, 0, 2]))  # 2,1,2 #5
    print(init.candy([1, 2, 2]))  # 1,2,1 #4
    print(init.candy([5, 4, 3, 5, 6, 2]))  # 9
