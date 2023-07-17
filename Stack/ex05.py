print("******** Parking Lot ********")

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)


inp = input("Enter max of car, car in soi, operation: ").split(" ")
max_car = int(inp[0])

if inp[1] == "0":
    car_in = Stack()
else:
    car_in = Stack()
    cars = inp[1].split(",")
    for car in cars:
        car_in.push(int(car))

operation = inp[2].split()
car_added = int(inp[3])

car_out = []

for i in operation:
    if i == "arrive":
        if car_in.size() < max_car and car_added not in car_in.stack:
            car_in.push(car_added)
            print("car", car_added, "arrive! : Add Car", car_added)
        elif car_added in car_in.stack:
            print("car", car_added, "already in soi")
        elif car_in.size() >= max_car:
            print("car", car_added , "cannot arrive: Soi Full")
        
    elif i == "depart":
        if car_in.is_empty():
            print("car", car_added, "cannot depart: Soi Empty")
        elif car_added not in car_in.stack:
            print("car", car_added, "cannot depart: Don't Have Car", car_added)
        else:
            car_in.stack.remove(car_added)
            print("car", car_added, "depart! : Car", car_added, "was removed")

while not car_in.is_empty():
    car_out.append(car_in.pop())

car_out.reverse()
print(car_out)
