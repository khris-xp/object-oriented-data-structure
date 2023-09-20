def insertion_sort(lst):
    lst_copy = lst[:]
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j > 0 and lst[j - 1] > current:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = current
    return lst, lst_copy

n = str(input("Enter Input : "))
n = n.split()
input_list = [int(i) for i in n]

sorted_list, original_list = insertion_sort(input_list)

if sorted_list == original_list:
    print("Yes")
else:
    print("No")