from typing import List


class AntOnTheBoundary:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        tot = 0
        for num in nums:
            tot += num
            if tot == 0:
                count += 1
        return count


if __name__ == '__main__':
    init = AntOnTheBoundary()
    print(init.returnToBoundaryCount([2, 3, -5]))  # 1
    print(init.returnToBoundaryCount([3, 2, -3, -4]))  # 0
