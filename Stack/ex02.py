stack_input = input("Enter Input : ").split(",")
stack = []
new_stack_list = []

for i in stack_input:
    if i[0] == "A":
        stack.append(i[2:])
        print("Add = " + i[2:])
    elif i[0] == "P":
        if len(stack) > 0:
            print("Pop = " + stack.pop())
        else:
            print("-1")
    elif i[0] == "D":
        if (len(stack) > 0):
            for j in range(len(stack)):
                last_items = stack.pop()
                if (last_items != i[2:]):
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items))
        else:
            print("-1")
    elif i[0] == 'L' and i[1] == 'D':
        if (len(stack) > 0):
            for j in range(len(stack)):
                last_items = stack.pop()
                if (int(last_items) >= int(i[2:])):
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is less than" + str(i[2:]))
        else:
            print("-1")
    elif i[0] == 'M' and i[1] == 'D':
        if (len(stack) > 0):
            for j in range(len(stack)):
                last_items = stack.pop()
                if (int(last_items) <= int(i[2:])):
                    new_stack_list.append(last_items)
                else:
                    print("Delete = " + str(last_items) + " Because " + str(last_items) + " is more than" + str(i[2:]))
        else:
            print("-1")
    
    for k in range(len(new_stack_list)):
        stack.append(new_stack_list.pop())

if (len(stack) == 0):
    print("Value in Stack = []")
else:
    print("Value in Stack = [" + ", ".join(stack) + "]")