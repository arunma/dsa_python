class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key) + "->" + str(self.next)


class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])  # this is to protect against duplicate keys
        node = LinkedList(key, value)
        if len(self.map) == self.capacity:
            del_node = self.tail.prev
            self.remove(del_node)
            self.add(node)
        else:
            self.add(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.map[node.key]

    def add(self, node):

        prev_first_node = self.head.next
        node.next = prev_first_node
        prev_first_node.prev = node
        node.prev = self.head
        self.head.next = node

        self.map[node.key] = node  # this needs to be done after the node links have been setup


if __name__ == '__main__':
    init = LRUCache(2)
    print(init.put(1, 1))  # None
    print(init.put(2, 2))  # None
    print(init.get(1))  # 1
    print(init.put(3, 3))  # None
    print(init.get(2))  # -1
    print(init.put(4, 4))  # None
    print(init.get(1))  # -1
    print(init.get(3))  # 3
    print(init.get(4))  # 4

    init = LRUCache(1)
    print(init.put(2, 1))  # None
    print(init.get(2))  # 1

    init = LRUCache(2)
    print(init.put(2, 1))  # None
    print(init.put(1, 1))  # None
    print(init.put(2, 3))  # None
    print(init.put(4, 1))  # None
    print(init.get(1))  # -1
    print(init.get(2))  # 3

    init = LRUCache(2)
    init.put(2, 1)
    init.put(2, 2)
    print(init.get(2))
    init.put(1, 1)
    init.put(4, 1)
    print(init.get(2))

    init = LRUCache(2)
    init.get(2)
    init.put(2, 6)
    print(init.get(1))
    init.put(1, 5)
    init.put(1, 2)
    print(init.get(1))
    print(init.get(2))
