class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
    def __str__(self):
        return str(self.key)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)

        if self.root == None:
            self.root = node
            return

        prev = None
        temp = self.root

        while (temp != None):
            if temp.key > key:
                prev = temp
                temp = temp.left
            elif temp.key < key:
                prev = temp
                temp = temp.right
        
        if (prev.key > key):
            prev.left = node
        else:
            prev.right = node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def search(self, node, key):
        if node is None:
            return False

        if node.key == key:
            return True
        elif node.key > key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
        
    def search_key(self, key):
        return self.search(self.root, key)

    def minValueNode(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.minValueNode(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        return node

T = BST()
data = input("Enter Input : ").split("/")
inp = list(map(int, data[0].split()))
find_index = int(data[1])
for i in inp:
    root = T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print("Searching")
if (T.search_key(find_index)):
    print("Found")
else:
    print("Not Found")
print("--------------------------------------------------")
print("Delete :", find_index)
T.delete(T.root, find_index)
T.printTree(T.root)