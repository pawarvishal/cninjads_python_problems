# Problem: Remove x from string


def remove_x(string):
    ln = len(string)
    if ln == 0:
        return string

    small_output = remove_x(string[1:])
    if string[0] == 'x':
        return "" + small_output
    else:
        return string[0] + small_output


string = input()
print(remove_x(string))
