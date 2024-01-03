class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        copy = x
        reversed = 0
        while copy:
            reversed *= 10
            reversed += copy % 10
            copy = copy // 10
        return reversed == x


if __name__ == '__main__':
    init = PalindromeNumber()
    print(init.isPalindrome(x=121))  # True
    print(init.isPalindrome(x=-121))  # False
    print(init.isPalindrome(x=10))  # False
