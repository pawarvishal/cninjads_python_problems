# Check if the list sorted using recursion


def is_sorted(a, si):
    ln = len(a)
    if si == ln - 1 or si == ln:
        return True

    if a[si] > a[si + 1]:
        return False

    return is_sorted(a, si + 1)


n = int(input("Enter the list size : "))
numList = list(map(int, input().strip().split()))
print(is_sorted(numList, 0))
