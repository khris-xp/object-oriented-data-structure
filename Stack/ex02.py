class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0
    
    def push(self, item):
        return self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
stack = Stack()
new_list_stack = Stack()

stack_input = input("Enter Input : ").split(",")

for i in stack_input:
    if i[0] == "A":
        stack.push(i[2:])
        print("Add = " + str(i[2:]))
    elif i[0] == "P":
        if not stack.is_empty():
            print("Pop = " + stack.pop())
        else:
            print(-1)
    elif i[0] == "D":
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if int(last_items) != int(i[2:]):
                    new_list_stack.push(last_items)
                else:
                    print("Delete : " + str(last_items))
        else:
            print(-1)
    elif i[0] == "L" and i[1] == "D":
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if int(last_items) >= int(i[2:]):
                    new_list_stack.push(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is less than" + str(i[2:]))
        else:
            print(-1)
    elif i[0] == "M" and i[1] == "D":
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if int(last_items) <= int(i[2:]):
                    new_list_stack.push(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is more than" + str(i[2:]))
        else:
            print(-1)
    
    for k in range(new_list_stack.size()):
        stack.push(new_list_stack.pop())

if stack.is_empty():
    print("Value in Stack = []")
else:
    print("Value in Stack = [" + ", ".join(stack.stack) + "]")