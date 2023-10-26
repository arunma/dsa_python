from collections import Counter, defaultdict
from typing import *


class SubstringWithConcatenationOfAllWords:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = Counter(words)
        word_len = len(words[0])
        N = len(s)
        num_words = len(words)

        result = []
        for i in range(word_len):
            matched = 0
            curr = defaultdict(int)
            start = i
            for j in range(i, N, word_len):
                word = s[j:j + word_len]
                if word not in words:
                    start = j + word_len
                    matched = 0
                    curr = defaultdict(int)
                    continue

                curr[word] += 1
                matched += 1

                while curr[word] > word_freq[word]:
                    start_word = s[start:start + word_len]
                    curr[start_word] -= 1
                    start = start + word_len
                    matched -= 1

                if matched == num_words:
                    result.append(start)
        return result


if __name__ == '__main__':
    init = SubstringWithConcatenationOfAllWords()
    print(init.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
    print(init.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))  # []
    print(init.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))  # [6,9,12]
    print(init.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]))  # [8]
