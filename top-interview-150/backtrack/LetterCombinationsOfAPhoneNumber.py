from typing import *


class LetterCombinationsOfAPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        mapp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.backtrack(digits, 0, mapp, result, '')
        return result

    def backtrack(self, digits, i, mapp, result, curr):
        if len(curr) == len(digits):
            result.append(curr)
        if i >= len(digits):
            return

        for c in mapp[digits[i]]:
            self.backtrack(digits, i + 1, mapp, result, curr + c)


if __name__ == '__main__':
    init = LetterCombinationsOfAPhoneNumber()
    print(init.letterCombinations(digits="23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(init.letterCombinations(digits=""))  # []
    print(init.letterCombinations(digits="2"))  # ["a","b","c"]
