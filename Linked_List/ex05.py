class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1
            self.tail = t

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        self.size += 1
        new_node = data
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, index, data):
        if index > self.size:
            return

        if index == 0:
            self.size += 1
            data.next = self.head
            self.head = data
            return

        if index == self.size:
            self.append(data)
            return

        self.size += 1
        new_node = data
        n = 0
        p = self.head
        last = self.head
        while n < index:
            n += 1
            last = p
            p = p.next

        last.next = new_node
        new_node.next = p

    def remove(self, data):
        if not self.isEmpty():
            if self.head.data == data:
                self.head = self.head.next
                self.size -= 1
            else:
                p = self.head
                while p.next is not None and p.next.data != data:
                    p = p.next
                p.next = p.next.next
                self.size -= 1

    def addHead(self, data):
        self.size += 1
        new_node = data
        new_node.next = self.head
        self.head = new_node

        p = self.head
        while p.next:
            p = p.next
        self.tail = p

    def removeHead(self):
        if not self.isEmpty():
            p = self.head
            self.size -= 1
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
            return p.data

    def addTail(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def removeTail(self):
        if not self.isEmpty():
            self.size -= 1
            p = self.head
            while True:
                if p.next == self.tail:
                    p.next = None
                    self.tail = p
                    break
                p = p.next

    def clear(self):
        self.head = self.tail = None

    def modify(self, group_len):
        new_list = List()

        p = self.head
        while p:
            i = 0
            lst = List()
            while p and i < group_len:
                lst.addHead(Node(p.data))
                p = p.next
                i += 1

            if new_list.isEmpty():
                new_list.head = lst.head
            else:
                new_list.tail.next = lst.head
            new_list.tail = lst.tail

            new_list.size += lst.size

        self.head = new_list.head

    def __len__(self):
        return self.size

    def __str__(self):
        ans = ""
        if self.head is None:
            return ans

        p = self.head
        has_alp = False
        while p.next:
            if str(p.data).isalpha():
                has_alp = True
                break
            p = p.next

        p = self.head
        while True:
            ans += str(p.data)
            if p.next is None:
                break
            if has_alp:
                ans += " > "
            else:
                ans += " <-> "
            p = p.next
        return ans


inp = input("Enter the elements of Linked list/group's size: ").split(" ")
isBlank = False

org = List()
mod = List()

if inp == [""]:
    print("No elements in Linked List ? OK!")
    print("Group' size should be greater than 0")

else:
    tmp = []
    if "/" in inp[-1]:
        tmp = inp[-1].split("/")

    if inp[-1][0] == "/" or int(tmp[-1]) <= 0:
        if inp[-1][0] == "/":
            print("No elements in Linked List ? OK!")
        if int(tmp[-1]) <= 0:
            print("Group' size should be greater than 0")
    else:
        for i in range(len(inp) - 1):
            org.append(Node(inp[i]))
            mod.append(Node(inp[i]))

        inp[-1] = inp[-1].split("/")
        inp[-1][-1] = int(inp[-1][-1])
        org.append(Node(inp[-1][0]))
        mod.append(Node(inp[-1][0]))

        print()
        mod.modify(inp[-1][-1])
        print("Original Linked list:", org)
        print("Modified Linked list:", mod)