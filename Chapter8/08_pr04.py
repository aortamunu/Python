def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)

s = sum(10)
print(s)