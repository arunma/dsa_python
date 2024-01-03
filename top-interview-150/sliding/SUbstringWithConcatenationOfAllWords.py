from collections import Counter, defaultdict
from typing import *


class SUbstringWithConcatenationOfAllWords:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = Counter(words)
        word_len = len(words[0])
        N = len(s)
        num_words = len(words)

        result = []
        for i in range(word_len):
            curr = defaultdict(int)
            start = i
            matched = 0
            for j in range(i, N, word_len):
                word = s[j:j + word_len]
                if word not in word_freq:
                    start = j + word_len  # TODO
                    curr = defaultdict(int)
                    matched = 0
                    continue

                curr[word] += 1
                matched += 1
                while curr[word] > word_freq[word]:
                    curr[s[start:start + word_len]] -= 1
                    start += word_len
                    matched -= 1

                if matched == num_words:
                    result.append(start)
        return result


if __name__ == '__main__':
    init = SUbstringWithConcatenationOfAllWords()
    print(init.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
    print(init.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))  # []
    print(init.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))  # [6,9,12]
    print(init.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]))  # [8]
