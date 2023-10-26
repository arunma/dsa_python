from typing import *


class SummaryRanges:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []

        cstart = nums[0]
        cend = nums[0]

        for num in nums:
            if num == cend or num == cend + 1:
                cend = num
            else:
                if cstart != cend:
                    result.append(f"{cstart}->{cend}")
                else:
                    result.append(f"{cstart}")
                cstart = num
                cend = cstart
        if cstart != cend:
            result.append(f"{cstart}->{cend}")
        else:
            result.append(f"{cstart}")
        return result

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []

        cstart = nums[0]
        cend = nums[0]

        for num in nums:
            if num == cend or num == cend + 1:
                cend = num
            else:
                if cstart != cend:
                    result.append(f"{cstart}->{cend}")
                else:
                    result.append(f"{cstart}")
                cstart = cend = num

        if cstart != cend:
            result.append(f"{cstart}->{cend}")
        else:
            result.append(f"{cstart}")
        return result


if __name__ == '__main__':
    init = SummaryRanges()
    print(init.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
    print(init.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]
