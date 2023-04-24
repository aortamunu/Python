n = int(input("Enter the number\n"))
print("*"* (n))
for i in range(1,n,2):
    print("*"*(n-(n-1))+" "*(n-2)+"*"*(n-(n-1)))

print("*"* (n))

