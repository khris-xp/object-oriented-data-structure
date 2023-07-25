class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0

    def push(self,item):
        return self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

stack = Stack()        
stack_invalid = False
stack_input = input("Enter arguments : ").split(" ")

for i in stack_input:
    if i == '+':
        if stack.size() >= 2:
            stack.push(int(stack.pop()) + int(stack.pop()))
    elif i == '-':
        if stack.size() >= 2:
            stack.push(int(stack.pop()) - int(stack.pop()))
    elif i == '*':
        if stack.size() >= 2:
            stack.push(int(stack.pop()) * int(stack.pop()))
    elif i == '/':
        if stack.size() >= 2:
            stack.push(int(stack.pop()) / int(stack.pop()))
    elif i == 'DUP':
        if stack.size() >= 1:
            stack.push(stack.stack[-1])
    elif i == 'POP':
        if stack.size() >= 1:
            stack.pop()
    elif i == 'PSH':
        if stack_input.index[i] + 1 < len(stack_input):
            value = stack_input[stack_input.index(i) + 1]
            if value.isnumeric():
                stack.push(int(value))
            else:
                stack.push(value)
    else:
        if i.isnumeric():
            stack.push(i)
        else:
            print("Invalid instruction: " + i)
            stack_invalid = True
            break

if stack.size() == 1:
    print(round(int(stack.stack[0])))
elif stack.size() > 1:
    print(stack.pop())
elif stack.size() == 0 and not stack_invalid:
    print(0)