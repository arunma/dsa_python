class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        i = N - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        if i < 0:
            return -1
        c = 0
        while i >= 0 and s[i] != ' ':
            c += 1
            i -= 1
        return c


if __name__ == '__main__':
    init = LengthOfLastWord()
    print(init.lengthOfLastWord("   fly me   to   the moon  "))
