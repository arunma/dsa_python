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


def build_a_bst(values):
    root = None
    for value in values:
        root = insert_into_bst(root, value)
    return root


def insert_into_bst(root, value):
    if not root:
        root = BinaryTreeNode(value)
        return root
    
    prev = None
    curr = root
    while curr:
        if value < curr.value:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    if value < prev.value:
        prev.left = BinaryTreeNode(value)
    else:
        prev.right = BinaryTreeNode(value)
    return root


if __name__ == '__main__':
    print(build_a_bst([7, 5, 9]))
