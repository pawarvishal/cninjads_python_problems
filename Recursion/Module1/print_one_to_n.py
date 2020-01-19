# print the numbers one to n recursively

def print_one_to_n(n):
    if n == 0:
        return
    print_one_to_n(n - 1)
    print(n)


n = int(input())
print_one_to_n(n)
