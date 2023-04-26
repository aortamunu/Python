file1 = 'this.txt'
file2 = 'copy.txt'

with open(file1) as f:
    f1content = f.read()

with open(file2) as f:
    f2content = f.read()

if f1content == f2content:
    print("The two files are identical.")
else:
    print("The two files are different.")