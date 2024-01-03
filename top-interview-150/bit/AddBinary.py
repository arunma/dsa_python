class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return a or b

        a = list(a)
        b = list(b)

        result = ""
        carry = 0
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            carry, value = divmod(carry, 2)
            result += str(value)
        return result[::-1]


if __name__ == '__main__':
    init = AddBinary()
    print(init.addBinary(a="11", b="1"))  # "100"
    print(init.addBinary(a="1010", b="1011"))  # "10101"
    print(init.addBinary(a="0", b="0"))  # "0"
    print(init.addBinary(a="0", b="1"))  # "1"
    print(init.addBinary(a="1", b="0"))  # "1"
