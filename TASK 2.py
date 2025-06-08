lis = [i for i in range(1, 11)]

sliced_list = lis[0:5]
sliced_list_copy = sliced_list[:]
sliced_list_copy.reverse()

print("Original list:", lis)
print("Extracted first five elements:", sliced_list)
print("Reversed extracted elements:", sliced_list_copy)

