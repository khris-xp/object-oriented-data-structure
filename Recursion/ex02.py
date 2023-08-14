def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

input_str = input("Enter Input : ")

if is_palindrome(input_str):
    print("'" + input_str + "'" + " is palindrome")
else:
    print("'" + input_str + "'" + " is not palindrome")