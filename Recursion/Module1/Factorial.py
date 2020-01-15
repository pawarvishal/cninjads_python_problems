# Calculate the Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    small_output = factorial(n-1)
    return n * small_output


num = int(input())
result = factorial(num)
print(result)