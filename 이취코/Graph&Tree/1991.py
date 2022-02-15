import sys

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end="")
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.data, end="")


n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    d, l, r = sys.stdin.readline().split()
    tree[d] = Node(d, l, r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])