# n = int(input("Enter the number that you want multiplication table of:\n"))
# i = 1
# for i in range(1, 11):
#     # print(str(n) + " x " + str(i) + " = " + str(n*i))
#     print(f"{n}x{i}={n*i}")


def mulTable(n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")
    
mt = mulTable(5)
print(mt)
