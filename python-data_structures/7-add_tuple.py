def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize the first two elements of tuple_a and tuple_b to 0
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add the first two elements of a and b
    new_tuple = (a[0] + b[0], a[1] + b[1])

    return new_tuple
