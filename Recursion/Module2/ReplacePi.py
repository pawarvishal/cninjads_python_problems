# Replace pi with 3.14 using recursion


def replace_pi(s):
    ln = len(s)
    if ln == 0 or ln == 1:
        return s

    if s[0] == 'p' and s[1] == 'i':
        return "3.14" + replace_pi(s[2:])
    else:
        return s[0] + replace_pi(s[1:])


s = input("Enter the string : ")
print(replace_pi(s))
