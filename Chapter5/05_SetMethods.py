b = set() #this syntax creates an empty SET
print(type(b)) 
print(b)

# Adding values to an empty set 
b.add(3)
b.add(5)
b.add(5)
b.add(5) #Even if we add something multiple times, Set would ignore all and just keep one. We would get {3,5} as output NOT {3, 5, 5, 5}
b.add(6)
b.add(8)
b.add(10)

print(b)

# b.add([2, 3, 5]) #this throws an ERROR because we cannot add List inside Set because List is unhashable meaning it can be changed in future. It is mutable(content of List is changeable)

b.add((2, 3, 5)) #Tuple can be added inside Set because Tuple is hashable meaning its value does not change during its lifetime. It is immutable

# b.add({2:3}) #Cannot add Dictionaries inside Set as it is unhashable too.
print(b)

print(len(b))


#Removal of an item
b.remove(5) #removes 5 from set 'b'
print(b)

print(b.pop())
print(b)
