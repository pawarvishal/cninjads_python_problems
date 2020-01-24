# Check if the number is in list using recursion
from sys import setrecursionlimit


def check_number(arr, x):
    ln = len(arr)
    if ln == 1 and arr[0] != x:
        return False

    if arr[0] == x:
        return True
    return check_number(arr[1:n], x)


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if check_number(arr, x):
    print('true')
else:
    print('false')
