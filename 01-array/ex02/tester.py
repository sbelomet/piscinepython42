from load_image import ft_load


# Run loader and print array when available
arr = ft_load("landscape.jpg")
if arr is not None:
    print(arr)


# Print docstring
print("")
print("ft_load doc:\n", ft_load.__doc__)


# Error handling test: non-string path should produce an error (returns None)
res = ft_load(123)
if res is None:
    print("Non-string path test: passed")
else:
    print("Non-string path test: failed")
