class CalculateMoneyInLeetcodeBank:
    # def totalMoney(self, n: int) -> int:
    #     monday = 1
    #     days = 0
    #     total = 0
    #     while days < n:
    #         total += monday
    #         monday += 1
    #         days += 1
    #         if days % 7 == 0:
    #             monday = days // 7 + 1
    #     return total

    def totalMoney(self, n: int) -> int:
        (weeks, rem_days) = divmod(n, 7)

        start = 28
        end = 28 + (weeks * 7)

        total = 0
        total += (start + end) * (weeks // 2)
        monday = weeks + 1
        for i in range(rem_days):
            total += monday + i

        return total


if __name__ == '__main__':
    init = CalculateMoneyInLeetcodeBank()
    print(init.totalMoney(n=4))  # 10
    print(init.totalMoney(n=10))  # 37
    print(init.totalMoney(n=20))  # 96
