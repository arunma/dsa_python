class IntegerToRoman:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        result = []
        i = 0
        while num > 0:
            n = num % 10
            if n <= 3:
                result.append(ones[i] * n)
            elif n == 4:
                result.append(ones[i] + fives[i])
            elif n <= 8:
                result.append(fives[i] + ones[i] * (n - 5))
            elif n == 9:
                result.append(ones[i] + ones[i + 1])
            i += 1
            num //= 10
        return "".join(result[::-1])


if __name__ == '__main__':
    init = IntegerToRoman()
    print(init.intToRoman(1994))  # MCMXCIV
