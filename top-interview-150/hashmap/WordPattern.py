class WordPattern:
    def wordPattern(self, pattern: str, s: str) -> bool:
        PN = len(pattern)
        s = s.split()
        if len(s) != PN:
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        map = {}
        for i in range(PN):
            if pattern[i] in map and map[pattern[i]] != s[i]:
                return False
            elif pattern[i] not in map:
                map[pattern[i]] = s[i]
        return True


if __name__ == '__main__':
    init = WordPattern()
    print(init.wordPattern(pattern="abba", s="dog cat cat dog"))  # true
    print(init.wordPattern(pattern="abba", s="dog cat cat fish"))  # false
    print(init.wordPattern(pattern="aaaa", s="dog cat cat dog"))  # false

    print(init.wordPattern(pattern="abbc", s="dog cat cat dog"))  # false
