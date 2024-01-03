from typing import *


class CheckIfTwoStringArraysAreEquivalent:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if not word1 and not word2:
            return True
        elif not word1 or not word2:
            return False

        left = right = 0
        li = ri = 0

        while left < len(word1) and right < len(word2):
            if word1[left][li] != word2[right][ri]:
                return False

            if li == len(word1[left]) - 1:
                li = 0
                left += 1
            else:
                li += 1
            if ri == len(word2[right]) - 1:
                ri = 0
                right += 1
            else:
                ri += 1

        return left == len(word1) and right == len(word2)


if __name__ == '__main__':
    init = CheckIfTwoStringArraysAreEquivalent()
    # print(init.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))  # True
    # print(init.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))  # False
    print(init.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))  # True
    print(init.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddef"]))  # True
