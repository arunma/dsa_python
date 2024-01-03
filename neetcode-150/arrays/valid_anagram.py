from collections import Counter


class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter(s)
        # smap = defaultdict(int)
        # for c in s:
        #     smap[c] += 1
        # smap = {}
        # for c in s:
        #     if c not in smap:
        #         smap[c] = 1
        #     else:
        #         smap[c] += 1

        for c in t:
            if c not in smap:
                return False
            smap[c] -= 1
            if smap[c] < 0:
                return False

        return not any(smap.values())


if __name__ == '__main__':
    init = ValidAnagram()
    print(init.isAnagram(s="anagram", t="nagaram"))  # True
    print(init.isAnagram(s="rat", t="car"))  # False
    print(init.isAnagram(s="ab", t="a"))  # False
