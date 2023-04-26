#Use open function to read the content of a file.
# f  = open('sample.txt', 'r')
f  = open('sample.txt') #By default, the mode is 'r'.
# data = f.read() #Reads all the content of file
# data = f.read(5) #Reads only 5 contents of the file.
data = f.read(12) #Reads only 12 contents of the file.
print(data)
f.close()