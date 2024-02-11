import sys


class MinimumTimeToRevertWordToInitialStateI:
    # def minimumTimeToInitialState(self, word: str, k: int) -> int:
    #     n = len(word)
    #     initial_state = word
    #
    #     for t in range(1, n + 1):
    #         prefix_to_remove = word[:k]
    #         suffix_to_add = word[-k:]
    #         word = suffix_to_add + prefix_to_remove
    #
    #         if word == initial_state:
    #             return t
    #
    #     return -1  # If the loop completes without finding a solution

    def minimumTimeToInitialState(self, word, k):
        n = len(word)
        remaining = n % k
        if remaining == 0:
            return n // k
        elif remaining > k // 2:  # Corrected: check if remaining is greater than half of k
            return (n // k) * 2 + 1  # Remove more, add less in the first cycle
        else:
            return (n // k) * 2  # Remove less, add more in the first cycle


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    init = MinimumTimeToRevertWordToInitialStateI()
    print(init.minimumTimeToInitialState("abacaba", 3))  # 2
    print(init.minimumTimeToInitialState("abacaba", 4))  # 1
    print(init.minimumTimeToInitialState("abcbabcd", 2))  # 4
