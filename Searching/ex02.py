def check_longest_increasing_subsequence(data):
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

    return res

data_input = [int(e) for e in input('Data : ').split()]
print('longest increasing subsequence :', check_longest_increasing_subsequence(data_input))