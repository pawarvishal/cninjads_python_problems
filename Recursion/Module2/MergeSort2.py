# Merge Sort 2
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


def merge_sort(arr, start, end):
    ln = len(arr)

    if ln == 0 or ln == 1:
        return

    mid = (start + end) // 2

    a1 = arr[:mid]
    a2 = arr[mid:]

    merge_sort(a1, 0, len(a1))
    merge_sort(a2, 0, len(a2))
    merge(a1, a2, arr)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
merge_sort(arr, 0, n)
print(*arr)
