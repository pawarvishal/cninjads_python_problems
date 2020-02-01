# First Index Of the Number
from sys import setrecursionlimit


def first_index(arr, x):
    ln = len(arr)
    if ln == 0:
        return -1

    if arr[0] == x:
        return 0

    smaller_list_op = first_index(arr[1:n], x)
    if smaller_list_op == -1:
        return -1
    else:
        return smaller_list_op + 1


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(first_index(arr, x))
