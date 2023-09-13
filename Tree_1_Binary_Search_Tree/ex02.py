class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def insert(self, key):
        node = Node(key)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
        while (temp != None):
            if (temp.data > key):
                prev = temp
                temp = temp.left
            elif(temp.data < key):
                prev = temp
                temp = temp.right
        if (prev.data > key):
            prev.left = node
        else:
            prev.right = node

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)
    
    def descending(self, node):
        if node is not None:
            self.descending(node.right) 
            print(node.data, end=" ")
            self.descending(node.left)

    def ascending(self, node):
        if node is not None:
            self.ascending(node.left)
            print(node.data, end=" ")
            self.ascending(node.right)  

T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print("Descending: ", end="")
T.descending(T.root)
print()
print("Ascending: ", end="")
T.ascending(T.root)
print()