from typing import *


class TreeNode:
    def __init__(self, low, high, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val
        self.low = low
        self.high = high

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


class RangeSumQueryMutable:
    def __init__(self, nums: List[int]):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, low, high):
        node = TreeNode(low, high)
        if low == high:
            node.val = nums[low]
            return node
        else:
            mid = (node.low + node.high) // 2
            node.left = self.build_tree(nums, low, mid)
            node.right = self.build_tree(nums, mid + 1, high)
            node.val = node.left.val + node.right.val
            return node

    def update(self, index: int, val: int, node=None) -> None:
        if not node:
            node = self.root

        if node.low == node.high == index:
            node.val = val
            return

        mid = (node.low + node.high) // 2

        if index <= mid:
            self.update(index, val, node.left)
        else:
            self.update(index, val, node.right)

        node.val = node.left.val + node.right.val
        return

    def sumRange(self, left: int, right: int, node=None) -> int:

        if not node:
            node = self.root

        if node.low == left and node.high == right:
            return node.val

        mid = node.low + (node.high - node.low) // 2

        if right <= mid:
            return self.sumRange(left, right, node.left)
        elif left > mid:
            return self.sumRange(left, right, node.right)
        else:
            return self.sumRange(left, mid, node.left) + self.sumRange(mid + 1, right, node.right)


if __name__ == '__main__':
    init = RangeSumQueryMutable([1, 2, 3, 4, 5])
    print(init.root)
    print(init.sumRange(0, 2))  # 6
    print(init.sumRange(2, 4))  # 12
    init.update(3, 0)
    print(init.sumRange(2, 4))  # 8
