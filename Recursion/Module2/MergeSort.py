# Merge Sort


def merge(a1, a2, a):
    i = 0
    j = 0
    k = 0

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1

    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1


def merge_sort(a):
    ln = len(a)

    if ln == 0 or ln == 1:
        return

    mid = ln // 2

    a1 = a[:mid]
    a2 = a[mid:]

    merge_sort(a1)
    merge_sort(a2)
    merge(a1, a2, a)

    return a


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(merge_sort(arr))
