# Sum of list elements using recursion
from sys import setrecursionlimit


def sum_array(arr):
    ln = len(arr)
    if ln == 1:
        return arr[0]

    return arr[0] + sum_array(arr[1:n])


setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sum_array(arr))
