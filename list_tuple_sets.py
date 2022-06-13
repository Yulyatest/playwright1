# a = (23, 34.55, [34, 'test'], ('test1', 34))
# print(a)
# a = (23, 55)
# print(a)

# Lists - can add/remove elements; keep order; can be modified
list = ["Bob", "Rolf", "Anne"]
# Tuple - can't add/remove elements; keep order; cannot be modified
tuple = ("Bob", "Rolf", "Anne")
# Set - can add/remove elements, but can't duplicate them; don't keep order; cannot be modified
set = {"Bob", "Rolf", "Anne"}

print(list[0])
print(tuple[1])
print(tuple)
print(set)

# modify list:
list[1] = "Dick"
print(list)
# add to list/remove
list.append("Julia")
print(list)
list.remove("Bob")
print(list)
# add to set
set.add("Mary")
print(set)
