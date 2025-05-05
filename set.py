# Creating sets
print("\n--- Creating Sets ---")
set1 = {1, 2, 3, 4}
set2 = set(["apple", "banana", "cherry"])
empty_set = set()  # Note: {} creates a dictionary, not a set
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Empty Set: {empty_set}")

# Adding elements to a set
print("\n--- Adding Elements ---")
set1.add(5)
set1.update([6, 7, 8])  # Adding multiple elements
print(f"Set1 after adding elements: {set1}")

# Removing elements from a set
print("\n--- Removing Elements ---")
set1.discard(8)  # Removes 8 if it exists, no error if it doesn't
set1.remove(7)   # Removes 7, raises KeyError if it doesn't exist
print(f"Set1 after removing elements: {set1}")

# Accessing elements in a set
print("\n--- Accessing Elements ---")
for item in set2:
    print(item)

# Set operations
print("\n--- Set Operations ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union: {set_a | set_b}")  # Union
print(f"Intersection: {set_a & set_b}")  # Intersection
print(f"Difference (A - B): {set_a - set_b}")  # Difference


# Clearing a set
print("\n--- Clearing a Set ---")
set1.clear()
print(f"Set1 after clearing: {set1}")

# Set immutability with frozenset
print("\n--- Frozenset (Immutable Set) ---")
frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")
# frozen.add(4)  # This will raise an AttributeError since frozensets are immutable