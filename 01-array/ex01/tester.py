from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

# Test 1
print("Test1:")
print(slice_me(family, 0, 2))
print("")

# Test 2
print("Test2:")
print(slice_me(family, 1, -2))
print("")

# Test 3 -- single row
print("Test3:")
print(slice_me(family, 2, 3))
print("")

# Docstring test
print("Docstring for slice_me:\n", slice_me.__doc__)
print("")

# Error handling test: non-2D input should raise TypeError
try:
    slice_me([1, 2, 3], 0, 1)
except TypeError:
    print("Non-2D input test: passed")
else:
    print("Non-2D input test: failed")
