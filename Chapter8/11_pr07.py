def remove(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

text = "      Python is good     "
n = remove(text, "Python")
print(n)