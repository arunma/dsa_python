class LargestOddNumberInString:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ""


if __name__ == '__main__':
    init = LargestOddNumberInString()
    print(init.largestOddNumber(num="52"))  # "5"
    print(init.largestOddNumber(num="4206"))  # ""
    print(init.largestOddNumber(num="35427"))  # "35427"
