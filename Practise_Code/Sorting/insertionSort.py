def insertion_sort(list_input):
    size = len(list_input)

    for i in range(1, size):
        min_index = list_input[i]
        j = i - 1

        while j >= 0 and min_index < list_input[j]:
            list_input[j + 1] = list_input[j]
            j -= 1
        
        list_input[j + 1] = min_index

data = [2, 3 , 5 , 1 , 7 , 4 , 4 , 1 , 4 , 3 , 2, 6 , 0]
insertion_sort(data)
print(data)