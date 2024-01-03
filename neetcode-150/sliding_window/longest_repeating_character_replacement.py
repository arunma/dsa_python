from collections import defaultdict


class LongestRepeatingCharacterReplacement:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     freq_map = defaultdict(int)
    #     ws = 0
    #     max_len = float('-inf')
    #     for we in range(len(s)):
    #         freq_map[s[we]] += 1
    #         while (we - ws + 1) > k + max(freq_map.values()):
    #             freq_map[s[ws]] -= 1
    #             ws += 1
    #         max_len = max(max_len, we - ws + 1)
    #     return max_len

    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        ws = 0
        max_len = float('-inf')
        for we in range(len(s)):
            freq_map[s[we]] += 1
            if (we - ws + 1) > k + max(freq_map.values()):
                freq_map[s[ws]] -= 1
                ws += 1
            max_len = max(max_len, we - ws + 1)
        return max_len


if __name__ == '__main__':
    init = LongestRepeatingCharacterReplacement()
    print(init.characterReplacement(s="ABAB", k=2))  # 4
    print(init.characterReplacement(s="AABABBA", k=1))  # 4
    print(init.characterReplacement(s="AABA", k=0))  # 2
    print(init.characterReplacement(s="ABBB", k=2))  # 4
