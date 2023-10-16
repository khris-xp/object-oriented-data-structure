def binary_search(list_input, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if list_input[mid] == x:
            return mid
        
        elif list_input[mid] > x:
            return binary_search(list_input, low, mid - 1, x)

        else:
            return binary_search(list_input, mid + 1 , high , x)
        
    else:
        return -1
    
data = [ 2, 3, 4, 10, 40 ]
x = 2
 
result = binary_search(data, 0, len(data)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")