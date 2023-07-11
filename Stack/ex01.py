mark_input = input("Enter Input : ")
stack = []

opening = ["[", "("]
closing = ["]", ")"]

for i in mark_input:
    if i in opening:
        stack.append(i)
    elif i in closing:
        pos = closing.index(i)
        if ((len(stack) > 0) and (opening[pos] == stack[len(stack) - 1])):
            stack.pop()
        else:
            stack.append(i)

if (len(stack) == 0):
    print(0)
    print("Perfect ! ! !")
else:
    print(len(stack))