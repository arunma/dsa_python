from typing import *


class FindTheGridOfRegionAverage:
    # def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
    #     R, C = len(image), len(image[0])
    #     result = [[0] * C for _ in range(R)]
    #     for r in range(R):
    #         for c in range(C):
    #             result[r][c] = self.dfs(image, r, c, threshold, R, C)
    #     return result
    #
    # def dfs(self, image, r, c, threshold, R, C):
    #     if r < 0 or r >= R or c < 0 or c >= C:
    #         return 0
    #     if image[r][c] < threshold:
    #         return 0
    #     count = 1
    #     count += self.dfs(image, r + 1, c, threshold, R, C)
    #     count += self.dfs(image, r - 1, c, threshold, R, C)
    #     count += self.dfs(image, r, c + 1, threshold, R, C)
    #     count += self.dfs(image, r, c - 1, threshold, R, C)
    #     return count

    def dfs(self, r, c, region, R, C, threshold, visited, image, sr, sc):
        visited.add((r, c))
        region.append(image[r][c])

        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if -1 < nr < R and -1 < nc < C and (nr, nc) not in visited and (abs(image[r][c] - image[nr][nc]) <= threshold) and abs(
                    nr - sr) <= 2 and abs(nc - sc) <= 2:
                self.dfs(nr, nc, region, R, C, threshold, visited, image, sr, sc)

    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        result = [[0] * C for _ in range(R)]

        region_id = 0
        region_map = {}

        for r in range(R):
            for c in range(C):
                if (r + 3) > R or (c + 3) > C:
                    continue
                visited = set()
                if (r, c) not in visited:
                    region = []
                    self.dfs(r, c, region, R, C, threshold, visited, image, r, c)

                    if region:
                        avg_intensity = sum(region) // len(region)
                        region_map[region_id] = avg_intensity

                        # print("region_id", region_id)
                        # print("region" + str(region))
                        # print("avg_intensity", avg_intensity)

                        region_size, num_cols = divmod(len(region), C)
                        for i in range(region_size):
                            for j in range(num_cols):
                                result[r - i][c - j] = region_id

                        region_id += 1

        for r in range(R):
            for c in range(C):
                if result[r][c] is not None:
                    result[r][c] = region_map[result[r][c]]
                else:
                    result[r][c] = image[r][c]

        return result


if __name__ == '__main__':
    init = FindTheGridOfRegionAverage()
    print(init.resultGrid([[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], 3))  # [[9,9,9,9],[9,9,9,9],[9,9,9,9]]
    print(init.resultGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))  # [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
