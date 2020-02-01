# First Index Of the Number
from sys import setrecursionlimit


def first_index(arr, x, si):
    ln = len(arr)
    if si == ln:
        return -1

    if arr[si] == x:
        return si

    return first_index(arr, x, si+1)


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(first_index(arr, x, 0))
