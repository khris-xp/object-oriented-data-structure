def find_largest_recursive(list, start, last):
  if start == last:
    return start

  largest_index = find_largest_recursive(list, start + 1, last)

  if list[start] > list[largest_index]:
    return start
  else:
    return largest_index

def selection_sort(list, last):
  if last == 0:
    return list

  largest_index = find_largest_recursive(list, 0, last)

  if largest_index != last:
    list[last], list[largest_index] = list[largest_index], list[last]
    print("swap " + str(list[largest_index]) + " <-> " + str(list[last]) + " : " + str(list))

  return selection_sort(list, last - 1)
n = str(input("Enter Input : "))
n = n.split()
input_list = [int(i) for i in n]
print(selection_sort(input_list, len(input_list) - 1))