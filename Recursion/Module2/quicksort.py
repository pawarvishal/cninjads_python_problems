# Quick Sort
def partition(a, si, ei):
    pivot = a[si]

    # find number of elements smaller than pivot
    c = 0
    for i in range(si, ei+1):
        if a[i] < pivot:
            c += 1

    a[si + c], a[si] = a[si], a[si + c]
    pivot_index = si + c

    # Now pivot is at it's correct position, make sure elements to right of pivot
    # are smaller and left ones are greater than pivot

    i = si
    j = ei

    while i < j:
        if a[i] < pivot:
            i += 1
        elif a[j] > pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    return pivot_index


def quick_sort(a, si, ei):
    if si >= ei:
        return

    pivot_index = partition(a, si, ei)
    quick_sort(a, si, pivot_index - 1)
    quick_sort(a, pivot_index + 1, ei)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
quick_sort(arr, 0, len(arr) - 1)
print(*arr)
