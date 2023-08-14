def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

input_data = input("Enter Input a b : ").split(" ")

print(power(int(input_data[0]), int(input_data[1])))