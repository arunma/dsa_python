class LongestPalindromicString:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)
            longest = max(longest, odd, even, key=len)

        return longest

    def expand(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return s[low + 1:high]

    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            lodd, hodd = self.expand(s, i, i)
            leven, heven = self.expand(s, i, i + 1)
            if hodd - lodd > len(longest):
                longest = s[lodd:hodd]
            if heven - leven > len(longest):
                longest = s[leven:heven]

        return longest

    def expand(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return low + 1, high


if __name__ == '__main__':
    init = LongestPalindromicString()
    print(init.longestPalindrome(s="babad"))  # bab
    print(init.longestPalindrome(s="cbbd"))  # bb
    print(init.longestPalindrome(s="a"))  # a
    print(init.longestPalindrome(s="ac"))  # a
    print(init.longestPalindrome(s="bb"))  # bb
    print(init.longestPalindrome(s="ccc"))  # ccc
