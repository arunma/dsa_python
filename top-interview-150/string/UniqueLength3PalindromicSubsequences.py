class UniqueLength3PalindromicSubsequences:
    def countPalindromicSubsequence(self, s: str) -> int:
        start = {}
        end = {}

        uniques = set(s)
        for c in uniques:
            start[c] = s.find(c)
            end[c] = s.rfind(c)

        count = 0
        for c in uniques:
            count += len(set(s[start[c] + 1:end[c]]))
        return count


if __name__ == '__main__':
    init = UniqueLength3PalindromicSubsequences()
    print(init.countPalindromicSubsequence(s="aabca"))  # 3
    print(init.countPalindromicSubsequence(s="adc"))  # 0
    print(init.countPalindromicSubsequence(s="bbcbaba"))  # 4
