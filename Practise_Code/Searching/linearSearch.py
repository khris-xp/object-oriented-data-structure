def linear_search(list_input, find_index):
    size = len(list_input)

    for i in range(size):
        if list_input[i] == find_index:
            return i
        
    return "No Index Found"

arr = [2, 3, 4, 10, 40] 
x = 10

print(linear_search(arr, x))