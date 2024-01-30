from collections import deque


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.end = False
        self.children = {}

    def __str__(self):
        return f"{self.value} {self.end} {self.children}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return self.root.__str__()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.end = True
        # print(f"add node: {node}")

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        # iterate through all children from now on
        return self.count_words(node)

    def count_words(self, node):
        queue = deque([node])
        count = 0
        while queue:
            node = queue.popleft()
            if node.end:
                count += 1
            for c in node.children:
                queue.append(node.children[c])
        return count


def contacts(queries):
    trie = Trie()
    for query in queries:
        if query.startswith("add "):
            trie.add(query.replace("add ", ""))
            print(trie)
        elif query.startswith("find "):
            print(trie.find(query.replace("find ", "")))


if __name__ == '__main__':
    print(contacts(queries=['add hack', 'add hackerrank', 'find hac', 'find hak']))  # 2 0
