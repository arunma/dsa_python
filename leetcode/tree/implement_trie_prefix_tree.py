from collections import deque


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.end

    # def startsWith(self, prefix: str) -> bool:
    #     node = self.root
    #     for c in prefix:
    #         if c in node.children:
    #             node = node.children[c]
    #         else:
    #             return False
    #     return True
    def startsWith(self, prefix: str) -> list[str]:
        node = self.root
        init = ""
        for c in prefix:
            if c in node.children:
                init += c
                node = node.children[c]
            else:
                return []
        return self.find_words(node, init)

    def find_words(self, node, prefix):
        result = []
        queue = deque([(node, prefix)])
        while queue:
            node, prefix = queue.popleft()
            if node.end:
                result.append(prefix)
            for c in node.children:
                queue.append((node.children[c], prefix + c))
        return result


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns [app, apple] # true
    trie.insert("app")
    print(trie.search("app"))  # returns true
