from typing import *


class InterleaveString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if self.is_interleave(s1, s2, s3, 0, 0, 0):
            return True
        return False

    def is_interleave(self, s1, s2, s3, i, j, k):
        print(i, j, k)
        print(s1[i:], s2[j:], s3[k:])
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        if k >= len(s3):
            return False

        if i < len(s1) and j < len(s2) and s1[i] == s3[k] and s2[j] == s3[k]:
            if self.is_interleave(s1, s2, s3, i + 1, j, k + 1) or self.is_interleave(s1, s2, s3, i, j + 1, k + 1):
                return True
        elif i < len(s1) and s1[i] == s3[k]:
            if self.is_interleave(s1, s2, s3, i + 1, j, k + 1):
                return True
        elif j < len(s2) and s2[j] == s3[k]:
            if self.is_interleave(s1, s2, s3, i, j + 1, k + 1):
                return True
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if self.is_interleave(s1, s2, s3, 0, 0, 0, {}):
            return True
        return False

    def is_interleave(self, s1, s2, s3, i, j, k, memo):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        if k >= len(s3):
            return False

        result = False
        if i < len(s1) and j < len(s2) and s1[i] == s3[k] and s2[j] == s3[k]:
            result = (result or
                      self.is_interleave(s1, s2, s3, i + 1, j, k + 1, memo) or
                      self.is_interleave(s1, s2, s3, i, j + 1, k + 1, memo))
        elif i < len(s1) and s1[i] == s3[k]:
            result = result or self.is_interleave(s1, s2, s3, i + 1, j, k + 1, memo)
        elif j < len(s2) and s2[j] == s3[k]:
            result = result or self.is_interleave(s1, s2, s3, i, j + 1, k + 1, memo)
        memo[(i, j, k)] = result
        return result


if __name__ == "__main__":
    init = InterleaveString()
    print(init.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))  # true
    print(init.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))  # false
