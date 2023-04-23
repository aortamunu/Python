sub1 = int(input("Enter your marks of Subject1\n"))
sub2 = int(input("Enter your marks of Subject2\n"))
sub3 = int(input("Enter your marks of Subject3\n"))

sum = sub1+sub2+sub3

perc = (sum*100)/300
print(perc)

if(sub1 >= 33 and sub2>=33 and sub3>=33 and perc>=40):
    print("Congratulations! You are pass.")
else:
    print("Sorry, You failed.")