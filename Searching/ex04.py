def are_isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False

    char_map = {}
    seen_chars = set()

    for char1, char2 in zip(string1, string2):
        if char1 not in char_map:
            if char2 in seen_chars:
                return False
            char_map[char1] = char2
            seen_chars.add(char2)
        elif char_map[char1] != char2:
            return False

    return True

def main():
    string_input = input("Enter str1, str2: ").split(',')
    string1 = string_input[0].strip()
    string2 = string_input[1].strip()

    if are_isomorphic(string1, string2):
        print(f"{string1} and {string2} are Isomorphic")
    else:
        print(f"{string1} and {string2} are not Isomorphic")

if __name__ == "__main__":
    main()
