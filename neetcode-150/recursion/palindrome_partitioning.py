from typing import *


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.partition_inner(s, [], result)
        return result

    def partition_inner(self, s, curr, result):
        if not s:
            result.append(curr.copy())
            return

        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.partition_inner(s[i:], curr + [s[:i]], result)

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    init = PalindromePartitioning()
    print(init.partition("aab"))  # [["a","a","b"],["aa","b"]]
    print(init.partition("a"))  # [["a"]]
