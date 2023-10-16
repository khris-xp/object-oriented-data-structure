def bubble_sort(list_input):
    size = len(list_input)

    for i in range(size):
        for j in range(0 , size - i - 1):
            if list_input[j] > list_input[j + 1]:
                list_input[j + 1], list_input[j] = list_input[j], list_input[j + 1]

data = [2, 3 , 5 , 1 , 7 , 4 , 4 , 1 , 4 , 3 , 2, 6 , 0]
bubble_sort(data)
print(data)