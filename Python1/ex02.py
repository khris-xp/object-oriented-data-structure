print("*** multiplication or sum ***")
mul_input = input("Enter num1 num2 : ")
mul_array = list(map(int, mul_input.split()))
mul_answer = mul_array[0] * mul_array[1]
plus_answer = mul_array[0] + mul_array[1]

if(mul_answer > 1000):
    print("The result is " + str(plus_answer))
else:
    print("The result is " + str(mul_answer))