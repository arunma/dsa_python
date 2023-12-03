class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True
        return None

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

    def dfs(self, word: str, node) -> bool:
        if not word and node.end:
            return True
        if not word and not node.end:
            return False

        w = word[0]
        rem = word[1:] if len(word) > 1 else None
        if w != '.':
            if w not in node.children:
                return False
            else:
                return self.dfs(rem, node.children[w])
        else:
            for child in node.children.values():
                if self.dfs(rem, child):
                    return True
        return False


if __name__ == '__main__':
    init = WordDictionary()
    init.addWord("bad")
    init.addWord("dad")
    init.addWord("mad")
    print(init.search("pad"))  # False
    print(init.search("bad"))  # True
    print(init.search(".ad"))  # True
    print(init.search("b.."))  # True
