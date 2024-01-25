#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list.copy()
    # Check if idx is within the valid range
    if idx >= 0:
        if idx < len(new_list):
            # Replace the element at idx in the new list
            new_list[idx] = element
    # Return the new list
    return new_list


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
