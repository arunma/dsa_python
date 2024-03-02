from typing import *


class MakeStringASubsequenceUsingCyclicIncrements:
    # def canMakeSubsequence(self, str1: str, str2: str) -> bool:
    #     str1 = set(str1)
    #     str2 = set(str2)
    #     diff1 = str1 - str2
    #     diff2 = str2 - str1
    #
    #     if not diff2:
    #         return True
    #
    #     for c in diff1:
    #         for d in diff2:
    #             if self.one_step_away(ord(c), ord(d)):
    #                 return True
    #     return False
    #
    # def one_step_away(self, c, d):
    #     if (d % 26) - (c % 26) == 1:
    #         return True
    #     else:
    #         return False

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if self.is_one_step_away(str1[i], str2[j]):
                j += 1
            i += 1
        return j == len(str2)

    def is_one_step_away(self, c, d):
        oc = ord(c) - ord('a')
        od = ord(d) - ord('a')
        if oc == od or (oc + 1) % 26 == od % 26:
            return True
        return False


if __name__ == "__main__":
    init = MakeStringASubsequenceUsingCyclicIncrements()
    print(init.canMakeSubsequence("abc", "ad"))  # true
    print(init.canMakeSubsequence("jrg", "h"))  # true
    print(init.canMakeSubsequence("zc", "ad"))  # true
    print(init.canMakeSubsequence("zc", "ad"))  # true
    print(init.canMakeSubsequence("ab", "d"))  # false
    print(init.canMakeSubsequence("c", "b"))  # false
    print(init.canMakeSubsequence("f", "f"))  # true
    print(init.canMakeSubsequence("ff", "fg"))  # true
