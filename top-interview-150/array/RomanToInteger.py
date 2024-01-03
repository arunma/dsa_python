class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        N = len(s)
        result = 0
        for i in range(N - 1):
            if r2i[s[i]] < r2i[s[i + 1]]:
                result -= r2i[s[i]]
            else:
                result += r2i[s[i]]
        result += r2i[s[-1]]
        return result


if __name__ == '__main__':
    init = RomanToInteger()
    print(init.romanToInt("MCMXCIV"))
