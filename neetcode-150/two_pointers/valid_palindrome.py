class ValidPalindrome:
    # def isPalindrome(self, s: str) -> bool:
    #     left = 0
    #     right = len(s) - 1
    #     ascii_chars = set("abcdefghijklmnopqrstuvwxyz01234567890")
    #     while left <= right:
    #         if s[left].lower() == s[right].lower():
    #             left += 1
    #             right -= 1
    #         else:
    #             if s[left].lower() not in ascii_chars:
    #                 left += 1
    #             elif s[right].lower() not in ascii_chars:
    #                 right -= 1
    #             else:
    #                 return False
    #     return True

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    init = ValidPalindrome()
    print(init.isPalindrome(s="A man, a plan, a canal: Panama"))  # true
    print(init.isPalindrome(s="race a car"))  # false
    print(init.isPalindrome(s=" "))  # true
    print(init.isPalindrome(s="0P"))  # false
