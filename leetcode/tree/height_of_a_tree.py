class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def find_height(root):
    if not root:
        return 0
    max_height = 0
    queue = [(root, 0)]
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in node.children:
            queue.append((child, height + 1))

    return max_height


def find_height_dfs(node):
    if not node:
        return 0

    max_height = 0
    for child in node.children:
        max_height = max(max_height, 1 + find_height_dfs(child))

    return max_height


def find_height_dfs(node):
    result = [0]
    find_height_dfs_tail_call(node, 0, result)
    return result[0]


def find_height_dfs_tail_call(node, height, result):
    result[0] = max(result[0], height)
    for child in node.children:
        find_height_dfs_tail_call(child, height + 1, result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(5))
    root.children[2].children.append(TreeNode(4))
    print(find_height(root))
    print(find_height_dfs(root))
