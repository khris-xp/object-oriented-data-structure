print(" *** String count ***")
message_input = input("Enter message : ")
message_array = []
upper_count = 0
lower_count = 0
upper_array = []
lower_array = []

for i in range(0, len(message_input)):
    message_array.append(message_input[i])

for i in range(0, len(message_array)):
    if(message_array[i].isupper()):
        upper_count += 1
        if( message_array[i] not in upper_array):
            upper_array.append(message_array[i])
            upper_array.sort()
    elif(message_array[i].islower()):
        lower_count += 1
        if(message_array[i] not in lower_array):
            lower_array.append(message_array[i])
            lower_array.sort()

print("No. of Upper case characters : " + str(upper_count))
print("Unique Upper case characters : " + '  '.join(map(str, upper_array)))
print("No. of Lower case Characters : " + str(lower_count))
print("Unique Lower case characters : " + '  '.join(map(str, lower_array)))