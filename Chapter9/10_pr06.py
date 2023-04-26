with open("log.txt", 'r') as f:
    mine = f.read()

if 'python' in mine.lower():
    print("python is present")
else:
    print("python is NOT present") 