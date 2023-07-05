def hbd(number):
    def convert_to_base(number, base):
        converted_number = ""
        while number > 0:
            digit = number % base
            converted_number = str(digit) + converted_number
            number //= base
        return converted_number
    
    for base in range(2, number + 1):
        converted = convert_to_base(number, base)
        if converted == "21" or converted == "20":
            return base, converted
    return None

year = int(input("Enter year : "))
base, converted = hbd(year)

if base is not None:
    print(f"saimai is just {converted}, in base {base}!")
else:
    print("No base found where the input is equal to 21 or 20.")
