print("* Stack Calculator *")

inp = input("Enter arguments : ").split(" ")
stack_invalid = False
stack = []

def push(value):
    stack.append(value)

def pop():
    return stack.pop() if not isEmpty() else None

def size():
    return len(stack)

def isEmpty():
    return size() == 0

for i in inp:
    if i == "+":
        if size() >= 2:
            push(int(pop()) + int(pop()))

    elif i == "-":
        if size() >= 2:
            push(int(pop()) - int(pop()))
    
    elif i == "*":
        if size() >= 2:
            push(int(pop()) * int(pop()))
    
    elif i == "/":
        if size() >= 2:
            push(int(pop()) / int(pop()))
        
    elif i == "DUP":
        if size() >= 1:
            push(stack[-1])
    
    elif i == "POP":
        if size() >= 1:
            pop()

    elif i == "PSH":
        if inp.index(i) + 1 < len(inp):
            value = inp[inp.index(i) + 1]
            if value.isnumeric():
                push(int(value))
            else:
                push(value)

    else:
        if i.isnumeric():
            push(int(i))
        else:
            print("Invalid instruction: " + i)
            stack_invalid = True
            break

if size() == 1:
    print(round(stack[0]))
elif size() > 1:
    print(stack.pop())
elif size() == 0 and not stack_invalid:
    print(0)