nepaliDictionary = {
    "Mero" : "Mine.",
    "Timro" : "Yours.",
    "Hamro" : "Ours.",
    "Maya" : "Love.",
    "Ghar" : "Home."
}

print("Options to search from are: ", nepaliDictionary.keys())
a = input("Enter the Nepali Word\n")
print("The meaning of", a,"is", nepaliDictionary.get(a))