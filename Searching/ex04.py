# Python program to check if two strings are isomorphic
MAX_CHARS = 256

def areIsomorhic(string1, string2):
    m = len(string1)
    n = len(string2)

    if m != n:
        return False

    marked = [False] * MAX_CHARS

    map = [-1] * MAX_CHARS

    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False

            marked[ord(string2[i])] = True

            map[ord(string1[i])] = string2[i]

        elif map[ord(string1[i])] != string2[i]:
            return False

    return True

string_input = input("Enter str1,str2: ").split(',')
string1 = string_input[0]
string2 = string_input[1]

if areIsomorhic(string1, string2):
    print(string1, "and", string2, "are Isomorphic")
else:
    print(string1, "and", string2, "are not Isomorphic")