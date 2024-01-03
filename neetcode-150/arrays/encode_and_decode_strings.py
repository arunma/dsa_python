from typing import *


class EncodeAndDecodeStrings:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for each in strs:
            result += f"{len(each)}:{each}"
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            coli = s.find(":", i)
            length = int(s[i:coli])
            word = s[coli + 1:coli + 1 + length]
            result.append(word)
            i = coli + length + 1
        return result


if __name__ == '__main__':
    init = EncodeAndDecodeStrings()
    print(init.encode(strs=["Hello", "Worl"]))
    print(init.decode(s="5:Hello4:Worl"))
