# Check if the list sorted using recursion


def is_sorted(a):
    ln = len(a)
    if ln == 0 or ln == 1:
        return True

    if a[0] > a[1]:
        return False

    return is_sorted(a[1:n])


n = int(input("Enter the list size : "))
numList = list(map(int, input().strip().split()))
print(is_sorted(numList))
