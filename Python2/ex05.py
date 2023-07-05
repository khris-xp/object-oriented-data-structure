class funString:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

    def size(self):
        return len(self.input_string)
    
    def changeSize(self):
        return self.input_string.swapcase()
    
    def reverse(self):
        return self.input_string[::-1]
    
    def deleteSame(self):
        sort_array =  sorted("".join(set(self.input_string)))
        return "".join(sort_array)
    
string_input, number_condition = input("Enter String and Number of Function : ").split()

if number_condition == "1":
    print(funString(string_input).size())

if number_condition == "2":
    print(funString(string_input).changeSize())

if number_condition == "3":
    print(funString(string_input).reverse())

if number_condition == "4":
    print(funString(string_input).deleteSame())