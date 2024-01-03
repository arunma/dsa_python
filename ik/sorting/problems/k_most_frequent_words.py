from collections import Counter
from typing import *


# def k_most_frequent(k, words):
#     counter = Counter(words)
#     result = [(count, word) for word, count in counter.items()]
#     result.sort(key=lambda x: (-x[0], x[1]))
#     return [each[1] for each in result[:k]]

def k_most_frequent(k, words):
    counter = Counter(words)
    bucket = [[] for _ in range(len(words) + 1)]
    for word, count in counter.items():
        bucket[count].append(word)

    result = []
    full = False
    for bucket in reversed(bucket):
        if full:
            break
        for word in sorted(bucket):
            result.append(word)
            if len(result) == k:
                full = True
                break

    return result


if __name__ == '__main__':
    # print(k_most_frequent(4, ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare","taxi"]))  # ["car", "driver", "taxi", "bus"]
    # print(k_most_frequent(1, ["car", "car", "car", "car", "car", "car"]))
    print(k_most_frequent(3, ["night", "day", "day", "noon", "noon", "noon", "evening", "evening", "evening", "evening"]))
