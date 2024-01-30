class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.value)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


def build_balanced_bst(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return BinaryTreeNode(nums[0])

    low = 0
    high = len(nums) - 1
    return build_balanced_bst_inner(nums, low, high)


def build_balanced_bst_inner(nums, low, high):
    if low > high:
        return None
    mid = low + (high - low) // 2
    root = BinaryTreeNode(nums[mid])
    root.left = build_balanced_bst_inner(nums, low, mid - 1)
    root.right = build_balanced_bst_inner(nums, mid + 1, high)
    return root


if __name__ == '__main__':
    print(build_balanced_bst([8, 10, 12, 15, 16, 20, 25]))
