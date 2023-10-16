def bubbleSort(list_input):
    size = len(list_input)
    for i in range(size):
        for j in range(size - i -1):
            if list_input[j] > list_input[j + 1]:
                list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]

def binar_search_tree(list_input,low, high, find_index):
    if high >= low:
        mid = (high + low) // 2
        if list_input[mid] == find_index:
            return mid
        elif list_input[mid] > find_index:
            return binar_search_tree(list_input, low, mid - 1 , find_index)
        else:
            return binar_search_tree(list_input, mid + 1, high, find_index)

data = [5, 4, 2 ,5 ,7, 1, 4, 9]
find_index = 4
bubbleSort(data)
size = len(data)
print(binar_search_tree(data, 0, size - 1, find_index))