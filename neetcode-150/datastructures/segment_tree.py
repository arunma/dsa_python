from typing import *


class TreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.sum = 0

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.sum)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


# class SegmentTree:
#
#     def __init__(self, nums: List[int]):
#         self.root = self.build_tree(nums, 0, len(nums) - 1)
#
#     def build_tree(self, nums, low, high):
#         if low > high:
#             return
#         root = TreeNode(low, high)
#         if low == high:
#             root.sum = nums[low]
#             return root
#         mid = low + (high - low) // 2
#         root.left = self.build_tree(nums, low, mid)
#         root.right = self.build_tree(nums, mid + 1, high)
#         root.sum = root.left.sum + root.right.sum
#         return root
#
#     def update(self, index: int, val: int, node=None) -> None:
#         if not node:
#             node = self.root
#         if node.low == node.high:
#             node.sum = val
#             return
#
#         mid = node.low + (node.high - node.low) // 2
#         if index <= mid:
#             self.update(index, val, node.left)
#         else:
#             self.update(index, val, node.right)
#         node.sum = node.left.sum + node.right.sum
#
#     def query(self, L: int, R: int, node=None) -> int:
#         if not node:
#             node = self.root
#         if node.low == L and node.high == R:
#             return node.sum
#         mid = node.low + (node.high - node.low) // 2
#         if R <= mid:
#             return self.query(L, R, node.left)
#         elif L >= mid + 1:
#             return self.query(L, R, node.right)
#         else:
#             return self.query(L, mid, node.left) + self.query(mid + 1, R, node.right)

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, low, high):
        # if low > high:
        #     return
        node = TreeNode(low, high)
        if low == high:
            node.sum = nums[low]
            return node

        mid = low + (high - low) // 2
        node.left = self.build_tree(nums, low, mid)
        node.right = self.build_tree(nums, mid + 1, high)
        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, index: int, val: int, node=None) -> None:
        if not node:
            node = self.root

        if node.low == node.high:
            node.sum = val
            return

        mid = node.low + (node.high - node.low) // 2

        if index <= mid:
            self.update(index, val, node.left)
        else:
            self.update(index, val, node.right)

        node.sum = node.left.sum + node.right.sum

    def query(self, left: int, right: int, node=None) -> int:
        if not node:
            node = self.root

        if node.low == left and node.high == right:
            return node.sum

        mid = node.low + (node.high - node.low) // 2

        if right <= mid:
            return self.query(left, right, node.left)
        elif left >= mid + 1:
            return self.query(left, right, node.right)
        else:
            return self.query(left, mid, node.left) + self.query(mid + 1, right, node.right)


if __name__ == '__main__':
    init = SegmentTree([1, 2, 3, 4, 5])
    print(init.root)
    print(init.query(0, 2))  # 6
    print(init.query(2, 4))  # 12
    init.update(3, 0)
    print(init.query(2, 4))  # 8
    #
    # init = SegmentTree([-1, 2, 4])
    # print(init.query(0, 1))  # 1
    # print(init.query(1, 2))  # 6
    # init.update(2, 3)
    # print(init.query(0, 2))  # 5
