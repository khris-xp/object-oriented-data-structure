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
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __len__(self):
        return self.size()

mark_input = input("Enter Input : ")
stack = Stack()

opening = ["[", "("]
closing = ["]", ")"]

for i in mark_input:
    if i in opening:
        stack.push(i)
    elif i in closing:
        pos = closing.index(i)
        if ((len(stack) > 0) and (opening[pos] == stack.peek())):
            stack.pop()
        else:
            stack.push(i)
    
if (len(stack) == 0):
    print(0)
    print("Perfect ! ! !")
else:
    print(stack.size())