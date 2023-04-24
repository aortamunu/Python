number = int(input("Enter a number to print its multiplication table in reversed order: "))

for i in range(10, 0, -1):
    print(f"{number} x {i} = {number*i}")