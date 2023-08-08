class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            out = ""
            while current:
                out += str(current.data) + " "
                current = current.next
            return out
 
    def append(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
 
        return count

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
 
        return prev


my_list1 = LinkedList()
my_list2 = LinkedList()
merged_list = LinkedList()

merged_list = LinkedList()

inp = input("Enter Input (L1,L2) : ").split()
linked_list_split1 = inp[0].split("->")
linked_list_split2 = inp[1].split("->")

for i in linked_list_split1:
    my_list1.append((i))
    merged_list.append(i)

for i in linked_list_split2:
    my_list2.append(i)
    merged_list.append(i)

print("L1    :", my_list1)
print("L2    :", my_list2)

reversed_list2_head = my_list2.reverse(my_list2.head)
reversed_list2 = LinkedList()
reversed_list2.head = reversed_list2_head

last_node = my_list1.head
while last_node.next:
    last_node = last_node.next

last_node.next = reversed_list2.head

print("Merge :", my_list1)