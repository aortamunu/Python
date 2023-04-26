f = open("next.txt", "w")
f.write("Hello i am writing this and this is Seemana")
f.close()

f = open("next.txt", "a") #We need to append to add text, if we write again it will overwrite the previous text 
f.write("Hello22222 i am writing this and this is Seemana")
f.close() #The text will be added as many times as I press the run.

#Revising
# f = open("next.txt", 'r')
# data = f.read()
# print(data)
# f.close()