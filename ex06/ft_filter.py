def ft_filter(function, iterable):
    """
    Mimics the built-in filter() function.
    Yields items from iterable for which function(item) is True.
    If function is None, removes items that are False in a boolean context.
    """
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
