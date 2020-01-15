# Calculate power of a number. Find x to the power n (i.e. x^n)
def calculate_power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    small_output = calculate_power(x, n-1)
    return x * small_output


x, n = map(int, input().split())
if (0 <= x <= 8) and (0 <= n <= 9):
    print(calculate_power(x, n))
else:
    print(1)
