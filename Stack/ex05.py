print("******** Parking Lot ********")

inp = input("Enter max of car,car in soi,operation : ").split(" ")
max_car = int(inp[0])

if (inp[1] == "0"):
    car_in = []
else:
    car_in = inp[1].split(",")

car_in = [int(i) for i in car_in]
operation = inp[2].split()
car_added = int(inp[3])

car_out = []

for i in operation:
    if i == "arrive":
        if len(car_in) < max_car and car_added not in car_in:
            car_in.append(int(car_added))
            print("car", car_added, "arrive! : Add Car", car_added)
        elif car_added in car_in:
            print("car", car_added, "already in soi")
        elif len(car_in) >= max_car:
            print("car", car_added , "cannot arrive : Soi Full")
        
    elif i == "depart":
        if len(car_in) == 0:
            print("car", car_added, "cannot depart : Soi Empty")
        elif car_added not in car_in:
            print("car", car_added, "cannot depart : Dont Have Car", car_added)
        else:
            car_in.remove(car_added)
            print("car", car_added, "depart ! : Car", car_added, "was remove")

print(car_in)