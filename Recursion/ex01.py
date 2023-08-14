def find_max_recursive(arr):
    if len(arr) == 1:
        return int(arr[0])
    return max(int(arr[-1]), find_max_recursive(arr[:-1]))

input_data = input("Enter Input : ").split()

print("Max :", find_max_recursive(input_data))
