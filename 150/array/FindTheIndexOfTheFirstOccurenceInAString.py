class FindTheIndexOfTheFirstOccurenceInAString:
    def strStr(self, haystack: str, needle: str) -> int:
        H = len(haystack)
        N = len(needle)
        max_start = H - N + 1
        for s in range(max_start):
            if haystack[s] != needle[0]:
                continue
            elif haystack[s:s + N] == needle:
                return s
        return -1


if __name__ == '__main__':
    init = FindTheIndexOfTheFirstOccurenceInAString()
    # print(init.strStr(haystack="sadbutsad", needle="sad"))
    # print(init.strStr(haystack="leetcode", needle="leeto"))
    # print(init.strStr(haystack="hello", needle="ll"))
    print(init.strStr(haystack="a", needle="a"))
