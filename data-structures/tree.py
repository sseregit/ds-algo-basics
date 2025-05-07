class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    def count_node(self, node):
        if node is None:
            return 0
        return 1 + self.count_node(node.left) + self.count_node(node.right)

    def calc_height(self, node):
        if node is None:
            return -1

        left_height = self.calc_height(node.left)
        right_height = self.calc_height(node.right)
        return 1 + max(left_height, right_height)

root = BTNode('A')
root.left = BTNode('B')
root.right = BTNode('C')

root.left.left = BTNode('D')
root.left.right = BTNode('E')

root.right.left = BTNode('F')
root.right.right = BTNode('G')

print("Preorder Traversal:")
root.preorder(root)
print("\nInorder Traversal:")
root.inorder(root)
print("\nPostorder Traversal:")
root.postorder(root)

print("\nTotal number of nodes:", root.count_node(root))
print("Height of the tree:", root.calc_height(root))

