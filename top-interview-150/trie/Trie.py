class TrieNode:
    def __init__(self, val=None, end=False):
        self.val = val
        self.end = end
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(w)
            node = node.children[w]
        node.end = True
        return None

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True


if __name__ == '__main__':
    init = Trie()
    print(init.insert("apple"))  # None
    print(init.search("apple"))  # True
    print(init.search("app"))  # False
    print(init.startsWith("app"))  # True
    print(init.insert("app"))  # None
    print(init.search("app"))  # True
