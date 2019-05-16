class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)


def SumOfNodesatLeaf(root):
    print("root : " + str(root.data))
    sum = 0
    if not root:
        return 0
    else:
        if root.left is not None:
            sum = sum + SumOfNodesatLeaf(root.left)
        else:
            sum = sum + root.data
        if root.right is not None:
            sum = sum + SumOfNodesatLeaf(root.right)
        else:
            sum = sum + root.data
        return sum

def maxLength(root):
    leftDepth = 0
    rightDepth = 0
    if not root:
        return 0
    else:
        if root.left is not None:
            leftDepth = maxLength(root.left)
        if root.right is not None:
            rightDepth = maxLength(root.right)
        max_depth = max(leftDepth, rightDepth)
        return max_depth + 1

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print root.data
    in_order_print(root.right)


def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.left)
    pre_order_print(root.right)

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
binary_insert(r, Node(6))
in_order_print(r)
print("maxDepth :" +str(maxLength(r)))

print("SumOfNodesatLeaf : " + str(SumOfNodesatLeaf(r)))