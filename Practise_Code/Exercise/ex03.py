data = input("Enter input : ").split("/")
input_list = list(map(int, data[0].split()))
find_index= int(data[1])

def insertion_sort(list_input):
    size = len(list_input)
    for i in range(1, size):
        min_index = list_input[i]
        j = i - 1
        while j >= 0 and min_index < list_input[j]:
            list_input[j + 1] = list_input[j]
            j -= 1
        
        list_input[j + 1] = min_index

def binary_search(list_input, low, high, find_index):
    if high >= low:
        mid = (high + low) // 2

        if list_input[mid] == find_index:
            return mid
        elif list_input[mid] > find_index:
            return binary_search(list_input, low, mid - 1 , find_index)
        else:
            return binary_search(list_input, mid + 1, high, find_index)
        
    else:
        return "Not Found"
    
insertion_sort(input_list)
print(input_list)
result = binary_search(input_list, 0, len(input_list)-1, find_index)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")