words = ["apple", "banana", "cherry", "fig", "grape"]
n = 5
long_words = [word for word in words if len(word) > n]

print("Words longer than", n, ":", long_words)
