from itertools import zip_longest


class MergeStringAlternatively:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([x + y for x, y in zip_longest(word1, word2, fillvalue='')])


if __name__ == '__main__':
    init = MergeStringAlternatively()
    print(init.mergeAlternately("abc", "pqr"))
    print(init.mergeAlternately("abc", "pqrs"))
