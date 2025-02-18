tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = sorted(tuples, key=lambda x: x[-1])

print("Sorted list:", sorted_tuples)
