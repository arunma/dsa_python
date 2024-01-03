class Largest3SameDigitNumberInString:
    def largestGoodInteger(self, num: str) -> str:
        ws = 0
        max_num = "000"
        set = False
        for we in range(1, len(num)):
            if num[we] != num[ws]:
                ws = we

            if we - ws + 1 == 3:
                cand = num[ws:we + 1]
                if int(cand) >= int(max_num):
                    max_num = cand
                    set = True

        return max_num if set else ""


if __name__ == '__main__':
    init = Largest3SameDigitNumberInString()
    print(init.largestGoodInteger(num="6777133339"))  # 777
    print(init.largestGoodInteger(num="2300019"))  # 000
    print(init.largestGoodInteger(num="42352338"))  # ""
