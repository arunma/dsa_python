from random import randint


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False

        index = len(self.val_index)
        self.val_index[val] = index
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.val_index:
            rm_index = self.val_index[val]
            last_index = len(self.vals) - 1
            last_val = self.vals[last_index]

            self.val_index[last_val] = rm_index  # Missed this line
            del self.val_index[val]

            self.vals[rm_index], self.vals[last_index] = self.vals[last_index], self.vals[rm_index]
            self.vals.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        rd_index = randint(0, (len(self.vals) - 1))
        return self.vals[rd_index]


if __name__ == '__main__':
    # init = RandomizedSet()
    # print(init.insert(1))  # True
    # print(init.remove(2))  # False
    # print(init.insert(2))  # True
    # print(init.getRandom())  # 1 or 2
    # print(init.remove(1))  # True
    # print(init.insert(2))  # False
    # print(init.getRandom())  # 2

    init = RandomizedSet()
    print(init.insert(0))  # True
    print(init.insert(1))  # True
    print(init.remove(0))  # True
    print(init.insert(2))  # True
    print(init.remove(1))  # True
    print(init.getRandom())  # 2
