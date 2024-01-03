class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        N = len(s)
        left = 0
        right = N - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif left < N and right > -1 and s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    init = ValidPalindrome()
    print(init.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(init.isPalindrome("race a car"))  # False
    print(init.isPalindrome(" "))  # True
    print(init.isPalindrome(".,"))  # False
