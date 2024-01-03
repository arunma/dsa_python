class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def __str__(self):
        return str(self.val)
