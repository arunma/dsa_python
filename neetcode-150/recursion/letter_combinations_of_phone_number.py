from typing import *


class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.letter_combinations_inner(digits, 0, "", result, mapp)
        return result

    def letter_combinations_inner(self, digits, index, curr, result, mapp):
        if len(curr) == len(digits):
            result.append(curr)
            return

        for i in range(index, len(digits)):
            for c in mapp[digits[i]]:
                self.letter_combinations_inner(digits, i + 1, curr + c, result, mapp)


if __name__ == '__main__':
    init = LetterCombinationsOfPhoneNumber()
    print(init.letterCombinations(digits="23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(init.letterCombinations(digits=""))  # []
    print(init.letterCombinations(digits="2"))  # ["a","b","c"]
