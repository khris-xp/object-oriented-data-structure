class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data <= root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    def prinPreOrder(self):
        self._printPreOrder(self.root)

    def _printPreOrder(self, root):
        if root is not None:
            if root == self.root:
                print("Preorder :", end=" ")
            print(root.data, end=" ")
            self._printPreOrder(root.left)
            self._printPreOrder(root.right)

    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self, root):
        if root is not None:
            if root == self.root:
                print("Inorder :", end=" ")
            self._printInOrder(root.left)
            print(root.data, end=" ")
            self._printInOrder(root.right)

    def printPostOrder(self):
        self._printPostOrder(self.root)

    def _printPostOrder(self, root):
        if root is not None:
            if root == self.root:
                print("Postorder :", end=" ")
            self._printPostOrder(root.left)
            self._printPostOrder(root.right)
            print(root.data, end=" ")

    def Breadth(self):
        if self.root is None:
            return

        print("Breadth :", end=" ")
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

inp = input("Enter Input : ").split(" ")

tree = BinarySearchTree()
for i in inp:
    tree.insert(int(i))

tree.prinPreOrder()
print(" ")
tree.printInOrder()
print(" ")
tree.printPostOrder()
print(" ")
tree.Breadth()
