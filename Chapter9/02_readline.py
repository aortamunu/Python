f  = open('sample.txt') #By default, the mode is 'r'.

#reads first line only, if you write a paragraph without pressing Enter button whole paragraph will be displayed.
data = f.readline() 
print(data)
f.close()