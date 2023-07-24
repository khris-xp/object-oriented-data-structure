class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

inp = input("Enter Infix : ")

stack = Stack()
operations = set(['+', '-', '*', '/', '^', '(', ')'])
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
output = ""

for i in inp:
    if i not in operations:
        output += i
    elif i == '(':
        stack.push(i)
    elif i == ')':
        while stack.size() > 0 and stack.peek() != '(':
            output += stack.pop()
        stack.pop()
    else:
        while stack.size() > 0 and priority[i] <= priority[stack.peek()]:
            output += stack.pop()
        stack.push(i)

while stack.size() > 0:
    output += stack.pop()

print("Postfix : " + output)
