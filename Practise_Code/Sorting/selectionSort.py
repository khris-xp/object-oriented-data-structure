def selection_sort(list_input):
    size = len(list_input)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if list_input[j] < list_input[min_index]:
                min_index = j
        
        list_input[i], list_input[min_index] = list_input[min_index], list_input[i]

data = [2, 3 , 5 , 1 , 7 , 4 , 4 , 1 , 4 , 3 , 2, 6 , 0]

selection_sort(data)
print(data)