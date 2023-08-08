class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            out = ""
            while current:
                out += str(current.data)
                if current.next:
                    out += "->"
                current = current.next
            return out
        
    def str_reverse(self):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            while current.next:
                current = current.next
            out = ""
            while current:
                out += str(current.data)
                if current.previous:
                    out += "->"
                current = current.previous
            return out

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            current.next.previous = current

        self.length += 1

    def insert(self, index, data):
        if index < 0:
            return "Data cannot be added"
        elif index == 0:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
            if temp:
                temp.previous = self.head
            self.length += 1
        elif index > self.length:
            return "Index out of range"
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            temp = current.next
            current.next = Node(data)
            current.next.next = temp
            current.next.previous = current
            if temp:
                temp.previous = current.next
            self.length += 1

    def remove(self, data):
            current = self.head
            index = 0
            while current:
                if current.data == data:
                    if index == 0:
                        self.head = self.head.next
                        if self.head:
                            self.head.previous = None
                    else:
                        current.previous.next = current.next
                        if current.next:
                            current.next.previous = current.previous
                    self.length -= 1
                    return index
                current = current.next
                index += 1
            return -1

    def __len__(self):
        return self.length
    
inp = input("Enter Input : ").split(",")
my_list = LinkedList()

for i in range(len(inp)):
    inp[i] = inp[i].strip().split()
    if inp[i][0] == "A":
        my_list.append(int(inp[i][1]))

        print("linked list :", my_list)
        print("reverse :", my_list.str_reverse())

    elif inp[i][0] == "Ab":
        my_list.insert(0, int(inp[i][1]))

        print("linked list :", my_list)
        print("reverse :", my_list.str_reverse())

    elif inp[i][0] == "I":

        insert_inp = inp[i][1].split(":")
        my_list.insert(int(insert_inp[0]), int(insert_inp[1]))

        if int(insert_inp[0]) > my_list.length or int(insert_inp[0]) < 0:
            print("Data cannot be added")
        else:
            print("index = {} and data = {}".format(insert_inp[0], insert_inp[1]))
        
        if my_list.length == 0:
            print("linked list :")
            print("reverse :")

        else:
            print("linked list :", my_list)
            print("reverse :", my_list.str_reverse())

    elif inp[i][0] == "R":
        index_removed = my_list.remove(int(inp[i][1]))
        if index_removed == -1:
            print("Not Found!")
        else:
            print("removed : {} from index : {}".format(inp[i][1], index_removed))
        if my_list.length == 0:
            print("linked list :")
            print("reverse :")
        else:
            print("linked list :", my_list)
            print("reverse :", my_list.str_reverse())