def find_min_index(matrix_input):
    min_index = 0
    for i in range(1, len(matrix_input)):
        if matrix_input[i] < matrix_input[min_index]:
            min_index = i
    return min_index

def find_max_index_in_row(matrix_input, min_index):
    max_index = 0
    for i in range(col):
        idx = row * min_index + i
        if idx < len(matrix_input) and matrix_input[idx] > matrix_input[max_index]:
            max_index = idx
    return max_index


def find_max_index_in_col(matrix_input, max_index_input):
    max_index = 0
    for i in range(row):
        idx = row * i + max_index_input
        if idx < len(matrix_input) and matrix_input[idx] > matrix_input[max_index]:
            max_index = idx
    return max_index

table, matrix_input = input("input : ").split(",")
table = list(map(int, table.split()))
matrix_list = list(map(int, matrix_input.split()))
row, col = table[0], table[1]

min_index = find_min_index(matrix_list) // col
row_max_index = find_max_index_in_row(matrix_list,min_index)
col_max_index = find_max_index_in_col(matrix_list, row_max_index % row)
print(matrix_list[col_max_index])