n = int(input("Enter the number of time you want to print stars\n"))
for i in range(n):
    print(" "* (n-i-1), end ="")
    print("*"* (2*i+1), end ="")
    print(" "* (n-i-1))
else:
    for i in range(n):
        print(" "* (n-1), end ="")
        print("*"* (1), end ="")
        print(" "* (n-1))
    

