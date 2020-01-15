# Calculate sum of n numbers
def sum_n(n):
    if n == 0:
        return 0
    small_output = sum_n(n-1)
    output = small_output + n
    return output


num = int(input())
print(sum_n(num))