class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2
    
    def multiply(self):
        return self.number1 * self.number2
    
    def divide(self):
        return self.number1 / self.number2
    
number1, number2 = input("Enter num1 num2 : ").split(",")
number1, number2 = int(number1), int(number2)
print(Calculator(number1, number2).add())
print(Calculator(number1, number2).subtract())
print(Calculator(number1, number2).multiply())
print(Calculator(number1, number2).divide())