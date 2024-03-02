from typing import *


class MaximumNumberOfBooksYouCanTake:
    # def maximumBooks(self, books: List[int]) -> int:
    #     N = len(books)
    #     dp = [0] * N
    #     stack = []
    #     for i in range(N):
    #         if not stack:
    #             stack.append(i)
    #             continue
    #         while stack:
    #             if books[i] > books[i - 1]:
    #                 val = min(books[i - 1], books[i] - 1)
    #                 dp[i] = books[i] + val

    def maximumBooks(self, books: List[int]) -> int:
        N = len(books)
        max_books = float('-inf')
        for i in range(N):
            prev_taken = books[i]
            curr_so_far = prev_taken
            for j in range(i - 1, -1, -1):
                curr = min(books[j], prev_taken - 1)
                if curr < 1:
                    break
                curr_so_far += curr
                prev_taken = curr
            max_books = max(curr_so_far, max_books)
        return max_books

    def maximumBooks(self, books: List[int]) -> int:
        N = len(books)
        max_books = [0] * N
        max_books[0] = books[0]
        result = float('-inf')
        for i in range(N):
            prev = books[i]
            curr_so_far = prev
            for j in range(i - 1, -1, -1):
                if books[j] <= prev - 1:
                    curr_so_far += max_books[j]
                    break
                else:
                    curr = min(books[i], prev - 1)
                    if curr < 1:
                        break
                    curr_so_far += curr
                    prev = curr
            max_books[i] = curr_so_far
            result = max(result, curr_so_far)
        # print(max_books)
        return result


if __name__ == "__main__":
    init = MaximumNumberOfBooksYouCanTake()
    print(init.maximumBooks([8, 5, 2, 7, 9]))  # 19
    print(init.maximumBooks([7, 0, 3, 4, 5]))  # 12
