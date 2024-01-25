def replace_in_list(my_list, idx, element):
    if idx >= 0:
        if idx < len(my_list):
            my_list[idx] = element
    return my_list
