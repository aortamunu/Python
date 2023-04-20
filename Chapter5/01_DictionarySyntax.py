myDictionary = {
    "Fast" : "In a quick manner.",
    "Seemana" : "A girl",
    "Marks" : [4,7,2,9,1,8],  #We can keep list too, in value of a key
    "anotherDictionary" : {'Seemana': 'An IT Student'} #We can make nested dictionaries too, this way
}

# print(myDictionary["Seemana"])
print(myDictionary["anotherDictionary"]['Seemana'])
print(myDictionary["Seemana"])
myDictionary["Seemana"] = "A girl with dreams" #A Python Dictionary is Mutable i.e. it can be changed like this ^^^
print(myDictionary["Seemana"])