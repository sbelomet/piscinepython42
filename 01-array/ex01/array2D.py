def slice_me(family: list, start: int, end: int) -> list:
    """Return a sliced 2D array and print original/new shapes.

    Args:
        family: 2D list (list of lists) of numeric values.
        start: start index for slicing (inclusive).
        end: end index for slicing (exclusive, may be negative).

    Returns:
        The sliced 2D list using Python slicing.

    Raises:
        TypeError: if arguments are not of expected types.
        ValueError: if rows are not the same length.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    # empty family
    if len(family) == 0:
        print("My shape is : (0, 0)")
        print("My new shape is : (0, 0)")
        return []

    # validate rows and determine number of columns
    cols = None
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a 2D list (list of lists)")
        if cols is None:
            cols = len(row)
        elif len(row) != cols:
            raise ValueError("all rows must have the same length")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("array elements must be int or float")

    rows = len(family)
    print(f"My shape is : ({rows}, {cols})")

    # slicing (uses Python slice semantics)
    new = family[start:end]
    print(f"My new shape is : ({len(new)}, {cols})")
    return new
