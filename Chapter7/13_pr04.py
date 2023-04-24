number = int(input("Enter the number to check for prime:\n"))
prime = True

for i in range(2,number):
    if(number%i==0):
        prime = False
        break
if prime:
    print("The number is Prime.")
else:
    print("The number is not Prime.")