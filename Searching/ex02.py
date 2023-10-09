data = [int(e) for e in input('Data : ').split()]
res = 0
index = seq = 1
stack = []

for n in data:
    if stack:
        while stack[-1] >= n:
            stack.pop(-1)
            if not stack:
                break
    stack.append(n)
    print(index, stack, sep=" : ")
    res = max(res, len(stack))
    index += 1

print('longest increasing subsequence :', res)