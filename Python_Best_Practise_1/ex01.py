print(" *** BMI ***")
weight_input, height_input = (float(a) if '.' in a else int(a) for a in input("Enter your weight(kg) and height(m) : ").split())

bmi_value = weight_input / (height_input * height_input)

if (bmi_value < 18.5):
    print("Your status is : Below normal weight.")
elif (bmi_value >= 18.5 and bmi_value < 25):
    print("Your status is : Normal weight.")
elif (bmi_value >= 25 and bmi_value < 30):
    print("Your status is : Overweight.")
elif (bmi_value >= 30 and bmi_value < 35):
    print("Your status is : Case I Obesity.")
elif (bmi_value >= 35 and bmi_value < 40):
    print("Your status is : Case II Obesity.")
elif (bmi_value >= 40):
    print("Your status is : Case III Obesity.")