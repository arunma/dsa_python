class DecodeWays:
    # def numDecodings(self, s: str) -> int:
    #     char_map = {(ord(c) - ord('A') + 1, c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    #     print("char_map", char_map)
    #     seen = {}
    #     return self.count_decodings(s, char_map, seen)
    #
    # def count_decodings(self, s, char_map, seen):
    #     if not s:
    #         return 1
    #     if s[0] == '0':
    #         return 0
    #     if s in seen:
    #         return seen[s]
    #
    #     count = 0
    #
    #     count += self.count_decodings(s[1:], char_map, seen)
    #     if len(s) > 1 and int(s[0:2]) <= 26:
    #         count += self.count_decodings(s[2:], char_map, seen)
    #     seen[s] = count
    #     return count

    def numDecodings(self, s: str) -> int:
        seen = {}
        return self.count_decodings(s, seen)

    def count_decodings(self, s, seen):
        if not s:
            return 1
        if s[0] == '0':
            return 0
        if s in seen:
            return seen[s]

        count = 0

        count += self.count_decodings(s[1:], seen)
        if len(s) > 1 and int(s[0:2]) <= 26:
            count += self.count_decodings(s[2:], seen)
        seen[s] = count
        return count


if __name__ == '__main__':
    init = DecodeWays()
    print(init.numDecodings(s="12"))  # 2
    print(init.numDecodings(s="226"))  # 3
    print(init.numDecodings(s="0"))  # 0
    print(init.numDecodings(s="06"))  # 0
    print(init.numDecodings(s="10"))  # 1
