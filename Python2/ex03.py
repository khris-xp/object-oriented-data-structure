print("*** Odd Even ***")
type_input, data_input, even_odd_input = input("Enter Input : ").split(",")
even_characters = []
odd_characters = []
data_array = list(map(str, data_input.split()))
if type_input == "S" and even_odd_input == "Even":
    for i in range(len(data_input)):
        if i % 2 != 0:
            even_characters.append(data_input[i])
    print("".join(even_characters))

if type_input == "S" and even_odd_input == "Odd":
    for i in range(len(data_input)):
        if i % 2 == 0:
            odd_characters.append(data_input[i])
    print("".join(odd_characters))

if type_input == "L" and even_odd_input == "Even":
    for i in range(len(data_array)):
        if i % 2 != 0:
            even_characters.append(data_array[i])
    
    print(even_characters)

if type_input == "L" and even_odd_input == "Odd":
    for i in range(len(data_array)):
        if i % 2 == 0:
            odd_characters.append(data_array[i])
    
    print(odd_characters)