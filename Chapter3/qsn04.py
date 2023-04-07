string =  "This is a  string with  double    spaces." #if we have two double spaces in a same place, there will remain one double space at last
st = string.replace("  ", " ")
print(st)