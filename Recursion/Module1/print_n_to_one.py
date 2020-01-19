# print the numbers n to one recursively

def print_n_to_one(n):
    if n == 0:
        return
    print(n)
    print_n_to_one(n - 1)


n = int(input())
print_n_to_one(n)
