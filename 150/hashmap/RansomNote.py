from collections import defaultdict


class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mmap = defaultdict(int)
        for m in magazine:
            mmap[m] += 1

        for r in ransomNote:
            if r not in mmap or mmap[r] - 1 < 0:
                return False
            mmap[r] -= 1

        return True


if __name__ == '__main__':
    init = RansomNote()
    print(init.canConstruct(ransomNote="a", magazine="b"))  # false
    print(init.canConstruct(ransomNote="aa", magazine="ab"))  # false
    print(init.canConstruct(ransomNote="aa", magazine="aab"))  # true
