from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        first = strs[0]
        last = strs[-1]
        N = len(first)
        i = 0
        for i, f in enumerate(first):
            if f == last[i]:
                i += 1
            else:
                return first[:i]
        return strs[0]


if __name__ == '__main__':
    init = LongestCommonPrefix()
    # print(init.longestCommonPrefix(strs=["flower", "flow", "flight"]))
    print(init.longestCommonPrefix(strs=["aba", "abc", "abab"]))
