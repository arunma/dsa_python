class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        S = len(s)

        for i, tc in enumerate(t):
            if si < S and s[si] == tc:
                si += 1

        return si == S


if __name__ == '__main__':
    init = IsSubsequence()
    print(init.isSubsequence(s="abc", t="ahbgdc"))  # true
    print(init.isSubsequence(s="axc", t="ahbgdc"))  # false
