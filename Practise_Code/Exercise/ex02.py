inp = [int(i) for i in input("Enter input: ").split()]
print("Before merged sort : ", inp)

def merged_sort(list_input):
    size = len(list_input)

    if (size > 1):

        left_list = list_input[:size//2]
        right_list = list_input[size//2:]

        merged_sort(left_list)
        merged_sort(right_list)

        #list index
        i = 0 #left index
        j = 0 #right index
        k = 0 #merged list index

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_input[k] = left_list[i]
                i += 1
            else:
                list_input[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list_input[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list_input[k] = right_list[j]
            j += 1
            k += 1

merged_sort(inp)
print("After merged : ", inp)