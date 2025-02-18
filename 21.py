list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 9, 10]

common = any(item in list1 for item in list2)
print("Do lists have a common item?", common)
