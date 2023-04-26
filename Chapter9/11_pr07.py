mine = True
i = 1

with open("log.txt", 'r') as f:
    
    while mine:
        mine = f.readline()

        if 'python' in mine.lower():
            print(mine)
            print(f"Yes python is present on line number {i}")
        i+=1