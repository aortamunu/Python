with open('poems.txt', 'w') as f:
    f.write("Hey I am writing a poem:\nTwinkle twinkle little star\nHow I wonder what you are..\nUp above the world so high...\nLike a diamond in the Skyyyyyyyyyy..........")

f = open('poems.txt', 'r')
t = f.read()
if "Twinkle" in t:
    print("Twinkle is present in the poem")
else:
    print("Twinkle is NOT present in the poem")

f.close()