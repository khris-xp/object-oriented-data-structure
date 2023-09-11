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

    def printFormatTree(self):
        self._printFormatTree(self.root, 0)
        print("--------------------------------------------------")

    def _printFormatTree(self, root, depth):
        if root is not None:
            self._printFormatTree(root.right, depth + 1)
            print(" " + "     " * depth + str(root.data))
            self._printFormatTree(root.left, depth + 1)

    def find_below(self, target):
        return self._find_below(self.root, target)

    def _find_below(self, root, target):
        if root is None:
            return 0
        if root.data <= target:
            cnt = 1
        else:
            cnt = 0
        cnt += self._find_below(root.left, target) + self._find_below(root.right, target)
        return cnt

inp = input("Enter Input : ").split("/")
data = list(map(int, inp[0].split()))
target = int(inp[1])

tree = BinarySearchTree()
for d in data:
    tree.insert(d)

tree.printFormatTree()

count = tree.find_below(target)
print(count)
