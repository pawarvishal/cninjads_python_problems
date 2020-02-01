# Replace char a with char b using recursion


def replace_char(s, a, b):
    ln = len(s)
    if ln == 0:
        return s

    small_output = replace_char(s[1:], a, b)
    if s[0] == a:
        return b + small_output
    else:
        return s[0] + small_output


s = input("Enter the string : ")
a = input("enter the char a: ")
b = input("enter the char b: ")
print(replace_char(s, a, b))
