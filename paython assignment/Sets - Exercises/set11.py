#11. Write a Python program to create a shallow copy of sets

set1 = set(["A", "B"])
set2 = set(["B", "D"])

set3 = set2.copy()
print(set3)
