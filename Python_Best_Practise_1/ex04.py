print("*** String Rotation ***")
strings_input = input("Enter 2 strings : ")
input_string1, input_string2 = strings_input.split()

string1 = input_string1
string2 = input_string2

count = 0
loop_count = 0
started_loop_1 = True
started_loop_2 = True

while (started_loop_1):
    string1 = string1[-1] + string1[:-1]
    string2 = string2[1:] + string2[0]
    loop_count += 1

    if(string1 == input_string1 and string2 == input_string2):
        started_loop_1 = False
        break

while (started_loop_2):
    string1 = string1[-1] + string1[:-1]
    string2 = string2[1:] + string2[0]
    count += 1
    print(str(count) + " " + str(string1) + " " + str(string2))
    if (string1 == input_string1 and string2 == input_string2):
        print("Total of  " + str(loop_count) + " rounds.")
        started_loop_2 = False
        break
    if(count == 5):
        if(string1[-1] + string1[:-1] == input_string1 and string2[1:] + string2[0] == input_string2):
            print(str(loop_count) + " " + str(input_string1) + " " + str(input_string2))
            print("Total of  " + str(loop_count) + " rounds.")
        else:
            print(" . . . . . ")
            print(str(loop_count) + " " + str(input_string1) + " " + str(input_string2))
            print("Total of  " + str(loop_count) + " rounds.")
        started_loop_2 = False
        break
