from typing import *

from TreeNode import *


class ConvertSortedArraytoBinarySearchTree:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        low = 0
        high = len(nums) - 1
        mid = low + (high - low) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    init = ConvertSortedArraytoBinarySearchTree()
    print(init.sortedArrayToBST([-10, -3, 0, 5, 9]))  # [0,-3,9,-10,null,5]
