class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_node(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = add_node(root.left, value)
    elif value > root.value:
        root.right = add_node(root.right, value)
    return root

def print_leaf_nodes(root):
    if root:
        print_leaf_nodes(root.left)
        if root.left is None and root.right is None:
            print(root.value, end=" ")
        print_leaf_nodes(root.right)

n = int(input())
numbers = list(map(int, input().split()))
tree_root = None
for i in range(len(numbers)):
    tree_root = add_node(tree_root, numbers[i])
print_leaf_nodes(tree_root)