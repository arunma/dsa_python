from collections import defaultdict


class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = float('-inf')
        freq_map = defaultdict(int)
        ws = 0
        for we in range(len(s)):
            freq_map[s[we]] += 1
            while freq_map[s[we]] > 1:
                freq_map[s[ws]] -= 1
                ws += 1
            max_length = max(max_length, we - ws + 1)
        return max_length


if __name__ == '__main__':
    init = LongestSubstringWithoutRepeatingCharacters()
    print(init.lengthOfLongestSubstring(s="abcabcbb"))  # 3
    print(init.lengthOfLongestSubstring(s="bbbbb"))  # 1
    print(init.lengthOfLongestSubstring(s="pwwkew"))  # 3
    print(init.lengthOfLongestSubstring(s=""))  # 0
    print(init.lengthOfLongestSubstring(s=" "))  # 1
