def weirdSubstract(number, round):
    number = str(number)
    i = 0

    while i < round:
        if number == "0":
            number = "0"
            break
        elif number[-1] == "0":
            number = number[:-1]
        else:
            number = str(int(number) - 1)
        i += 1

    return number

number_input, round_input = input("Enter num and sub: ").split()
print(weirdSubstract(number_input, int(round_input)))