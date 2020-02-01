# Binary Search


def binary_search(a, x, si, ei):
    if si > ei:
        return -1

    mid = (si + ei) // 2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, si, mid - 1)
    else:
        return binary_search(a, x, mid + 1, ei)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(binary_search(arr, x, 0, len(arr) - 1))
