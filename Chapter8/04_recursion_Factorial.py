# n = 5
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

def factorial_recursive(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial_recursive(n-1) #<--- function calling itself
# f = factorial_iter(4)
f = factorial_recursive(4)
print(f)

