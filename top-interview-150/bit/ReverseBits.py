class ReverseBits:
    def reverseBits(self, n: int) -> int:
        out = 0
        print(bin(n))
        for i in range(32):
            out <<= 1
            b = n & 1
            out = out ^ b
            n >>= 1
        print(bin(out))
        return out


if __name__ == '__main__':
    init = ReverseBits()
    print(init.reverseBits(n=0b00000010100101000001111010011100))
    print(init.reverseBits(n=0b11111111111111111111111111111101))
