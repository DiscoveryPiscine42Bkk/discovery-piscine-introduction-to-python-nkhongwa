original_array = [2,8,9,48,8,22,-12,2]
new_array = [x + 2 for x in original_array]
print("Original array:", original_array)
print("New array:", new_array)
filtered_array = [x for x in original if x >5]
print("filtered array (>5):", filtered_array)