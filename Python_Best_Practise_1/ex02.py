print(" *** Rank score ***")
id_score_input = input("Enter ID and Score end with ID : ")
id_score_array = list(map(str, id_score_input.split()))
new_id_score_array = list(map(str, id_score_input.split()))
count_array = 0
id_score_array.pop()

new_id_score_dict = {}

for i in range(0, len(id_score_array), 2):
    new_id_score_dict[id_score_array[i]] = float(id_score_array[i + 1])
    count_array += 1

print(id_score_array)
print(new_id_score_array[-1])
print(new_id_score_dict)
print(count_array - 1)