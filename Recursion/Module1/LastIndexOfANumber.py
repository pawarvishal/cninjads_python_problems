# Last Index Of the Number
from sys import setrecursionlimit


def last_index(arr, x):
    ln = len(arr)
    if ln == 0:
        return -1

    smaller_list_op = last_index(arr[1:n], x)

    if smaller_list_op != -1:
        return smaller_list_op + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(last_index(arr, x))
