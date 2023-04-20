myDictionary = {
    "Fast" : "In a quick manner",
    "Seemana" : "A girl",
    "Marks" : [4,7,2,9,1,8],  #We can keep list too, in value of a key
    "anotherDictionary" : {'Seemana': 'An IT Student'}, #We can make nested dictionaries too, this way
    1 : 2 #we can keep both integer key-value pairs too
}

# Methods of Python Dictionaries

print(myDictionary.keys())  # --> will print all the keys in dictionary in the form of list
print(type(myDictionary.keys())) # <class 'dict_keys'>, this is the default type
print(list(myDictionary.keys())) # can be typecasted into list
print(myDictionary.values()) #Prints the values of the dictionary
print(myDictionary.items()) #Prints (key,value) for all contents of the dictionary

print(myDictionary)
updateDictionary = {
    "Python": 'A programming language',  
    "Seemana": 'A brave girl'  #updates the existing values too. not by adding new, but replacing the existing
}
myDictionary.update(updateDictionary)  #Updates the dictionary by adding the key-value pairs from updateDictionary
print(myDictionary)


print(myDictionary.get("Seemana")) 
print(myDictionary["Seemana"])
#We cannot find any differences of using .get and [] syntax from above

#The difference between .get and [] syntax in dictionaries
print(myDictionary.get("Seemana1")) #returns 'none' as Seemana1 is not present in the dictionary
print(myDictionary["Seemana1"]) #it throws an error if the key is not present in the dictionary
