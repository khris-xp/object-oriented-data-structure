def sorted_drome(arr):
    digit_list = [int(digit) for digit in str(arr)]

    has_duplicates = len(digit_list) != len(set(digit_list))

    is_increase = all(digit_list[i] <= digit_list[i + 1] for i in range(len(digit_list) - 1))
    is_decrease = all(digit_list[i] >= digit_list[i + 1] for i in range(len(digit_list) - 1))
    
    for i in range(1, len(digit_list)):
        if has_duplicates and is_increase and not all(digit == digit_list[0] for digit in digit_list):
            status = "Plaindrome"
        elif is_increase and not all(digit == digit_list[0] for digit in digit_list) and not has_duplicates:
            status = "Metadrome"
        elif is_decrease and not all(digit == digit_list[0] for digit in digit_list) and not has_duplicates:
            status = "Katadrome"
        elif has_duplicates and is_decrease and not all(digit == digit_list[0] for digit in digit_list):
            status = "Nialpdrome"
        elif all(digit == digit_list[0] for digit in digit_list):
            status = "Repdrome"
        else:
            status = "Nondrome"

    return status

input_number = int(input("Enter Input : "))
print(sorted_drome(input_number))
