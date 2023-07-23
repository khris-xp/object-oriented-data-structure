class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()

inp = input("Enter Input : ").split(',')
new_stack_list = []

for i in inp:
    if i[0] == "A":
        stack.push(i[2:])
        print("Add = " + i[2:])
    elif i[0] == "P":
        if not stack.is_empty():
            print("Pop = " + stack.pop())
        else:
            print("-1")
    elif i[0] == "D":
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if last_items != i[2:]:
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items))
        else:
            print("-1")
    elif i[0] == 'L' and i[1] == 'D':
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if int(last_items) >= int(i[2:]):
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is less than" + str(i[2:]))
        else:
            print("-1")
    elif i[0] == 'M' and i[1] == 'D':
        if not stack.is_empty():
            for j in range(stack.size()):
                last_items = stack.pop()
                if int(last_items) <= int(i[2:]):
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is more than" + str(i[2:]))
        else:
            print("-1")
    
    for k in range(len(new_stack_list)):
        stack.push(new_stack_list.pop())

if stack.is_empty():
    print("Value in Stack = []")
else:
    print("Value in Stack = [" + ", ".join(stack.stack) + "]")