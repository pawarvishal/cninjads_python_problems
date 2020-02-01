# Last Index Of the Number
from sys import setrecursionlimit


def last_index(arr, x, si):
    ln = len(arr)
    if si == ln:
        return -1

    small_list_op = last_index(arr, x, si+1)

    if small_list_op != -1:
        return small_list_op
    else:
        if arr[si] == x:
            return si
        else:
            return -1


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(last_index(arr, x, 0))
