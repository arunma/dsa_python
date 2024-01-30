class NumerOfDicRollsWithTargetSum:
    # def numRollsToTarget(self, d: int, k: int, target: int) -> int:
    #     memo = {}
    #     return self.dp(d, k, target, memo)
    #
    # def dp(self, d, k, target, memo):
    #     if d == 0 and target == 0:
    #         return 1
    #     if d == 0 or target == 0:
    #         return 0
    #     if (d, target) in memo:
    #         return memo[(d, target)]
    #     ways = 0
    #     for i in range(1, k + 1):
    #         if target >= i:
    #             ways += self.dp(d - 1, k, target - i, memo)
    #     memo[(d, target)] = ways
    #     return ways

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        return self.num_rolls_to_target_inner(d, f, target, memo)

    def num_rolls_to_target_inner(self, d, f, target, memo):
        if d == 0 and target == 0:
            return 1
        if d == 0 or target == 0:  # the or target==0 is not required because of target>=ff
            return 0
        if (d, target) in memo:
            return memo[(d, target)]
        ways = 0
        for ff in range(1, f + 1):
            if target >= ff:
                ways += self.num_rolls_to_target_inner(d - 1, f, target - ff, memo)
        memo[(d, target)] = ways % (10 ** 9 + 7)
        return memo[(d, target)]


if __name__ == '__main__':
    init = NumerOfDicRollsWithTargetSum()
    print(init.numRollsToTarget(d=1, f=6, target=3))  # 1
    print(init.numRollsToTarget(d=2, f=6, target=7))  # 6
    print(init.numRollsToTarget(d=2, f=5, target=10))  # 1
