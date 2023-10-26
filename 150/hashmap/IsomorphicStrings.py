class IsomorphicStrings:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        hmap = {}
        for i in range(len(t)):
            if t[i] not in hmap:
                hmap[t[i]] = s[i]
            elif hmap[t[i]] != s[i]:
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmap = {}
        smap = {}
        for i in range(len(t)):
            se = s[i]
            te = t[i]
            if (se in smap and (te not in tmap or smap[se] != tmap[te])) or (te in tmap and (se not in smap or smap[se] != tmap[te])):
                return False

            smap[se] = i
            tmap[te] = i

        return True


if __name__ == '__main__':
    init = IsomorphicStrings()
    # print(init.isIsomorphic(s="egg", t="add"))  # true
    # print(init.isIsomorphic(s="foo", t="bar"))  # false
    print(init.isIsomorphic(s="paper", t="title"))  # true
    print(init.isIsomorphic(s="badc", t="baba"))  # false
    print(init.isIsomorphic(s="bara", t="fool"))  # false
