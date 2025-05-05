
# Creating tuples
my_tuple = ('orange', 'mango', 'banana', 'apple')
print("\n--- Tuple Basics ---")
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# Accessing tuple elements
print("\n--- Accessing Elements ---")
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])


duplicat_list = list(my_tuple)

duplicat_list.append('kiwi')
duplicat_list.insert(0, 'xyz')  # Fixed: Specify index 0 and value 'xyz'

updated_tuple = tuple(duplicat_list)
print(updated_tuple)


# Tuple methods
print("\n--- Tuple Methods ---")
repeated_tuple = (1, 2, 3, 1, 2, 1)
print(repeated_tuple.count(1))
print(repeated_tuple.index(2))

# Tuple concatenation
print("\n--- Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
combined = tuple1 + tuple2
print(combined)

# Nested tuples
print("\n--- Nested Tuples ---")
nested = ((1, 2), ('a', 'b'), (True, False))
print(nested)
print(nested[1][0])

# Converting list to tuple and back
print("\n--- Conversions ---")
list_to_convert = ['one', 'two', 'three']

converted_tuple = tuple(list_to_convert)
print(f"List {list_to_convert} converted to tuple: {converted_tuple}")
back_to_list = list(converted_tuple)
print(f"Tuple converted back to list: {back_to_list}")

# Printing tuple elements line by line
print("\n--- Printing Tuple Elements Line by Line ---")
print(*my_tuple, sep='\n')


