class Stack:
    def __init__(self, operations, priority, stack, output, expression):
        self.operations = operations
        self.priority = priority
        self.stack = stack
        self.output = output
        self.expression = expression
    
    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.size() == 0

inp = input("Enter Infix : ")

stack = Stack(None, None, None, None, None)

stack.operations = set(['+', '-', '*', '/', '(', ')', '^'])
stack.priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}
stack.stack = []
stack.output = ""

for i in inp:
    if i not in stack.operations:
        stack.output += i
    elif i == '(':
        stack.push(i)
    elif i == ')':
        while stack.size() > 0 and stack.stack[-1] != '(':
            stack.output += stack.stack[-1]
            stack.pop()
        stack.pop()
    else:
        while stack.size() > 0 and stack.priority[i] <= stack.priority[stack.stack[-1]]:
            stack.output += stack.stack[-1]
            stack.pop()
        stack.push(i)

while stack.size() > 0:
    stack.output += stack.stack[-1]
    stack.pop()

print("Postfix : " + stack.output)