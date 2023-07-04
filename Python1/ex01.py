print("*** Converting hh.mm.ss to seconds ***")
time_input = input("Enter hh mm ss : ")
time_array = list(map(int, time_input.split()))

hours = time_array[0] * 3600
minutes = time_array[1] * 60
seconds = time_array[2]

seconds_total = hours + minutes + seconds

if(time_array[1] >= 60 or time_array[1] < 0):
    print("mm" + "(" + str((time_array[1])) + ")" + " is invalid!")
elif(time_array[2] >= 60 or time_array[2] < 0):
     print("ss" + "(" + str((time_array[1])) + ")" +  " is invalid!")
else:
    print(str(f"{time_array[0]:02}")+":"+str(f"{time_array[1]:02}")+":"+str(f"{time_array[2]:02}") + " = " + str(f"{seconds_total:,}") + " seconds")