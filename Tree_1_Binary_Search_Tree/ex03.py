class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, node, data):
        if data <= node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.insertNode(node.left, data)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.insertNode(node.right, data)

    def printFormatTree(self):
        BinarySearchTree._printFormatTree(self.root,0)
        print("--------------------------------------------------")
    
    def _printFormatTree(root,depth):
        if root is not None:
            BinarySearchTree._printFormatTree(root.getRight(),depth + 1)
            print(" " + "     " * depth + str(root.data))    
            BinarySearchTree._printFormatTree(root.getLeft(),depth + 1)

    def find_below(self,target):
        cnt = BinarySearchTree._find_below(self.root,target)
        return cnt
        

    def _find_below(root,target):
        if root is not None and root.getLeft() is None and root.getRight() is None:
            if root.data <= target:
                return 1
            else:
                return 0
            
        elif root is not None:
            if root.data > target:
                return BinarySearchTree._find_below(root.getLeft(),target)
            else:
                cnt1 = BinarySearchTree._find_below(root.getLeft(),target)
                cnt2 = BinarySearchTree._find_below(root.getRight(),target)
                return 1 + cnt1 + cnt2
        else:
            return 0
        
inp = input("Enter Input : ").split("/")

data = inp[0].split()
target = int(inp[1])

tree = BinarySearchTree()
data = [int(num) for num in data]


for d in data:
    tree.insert(d)

tree.printFormatTree()

count = tree.find_below(target)
print(count)