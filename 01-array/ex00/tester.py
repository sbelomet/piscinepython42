from give_bmi import give_bmi, apply_limit


# Test 1 -- original
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print("Test1 BMI:", bmi)
print("Test1 apply_limit:", apply_limit(bmi, 26))
print("")


# Test 2 -- single entry
height2 = [1.8]
weight2 = [80]
bmi2 = give_bmi(height2, weight2)
print("Test2 BMI:", bmi2)
print("Test2 apply_limit (25):", apply_limit(bmi2, 25))
print("")


# Docstring test
print(give_bmi.__doc__)
print(apply_limit.__doc__)
print("")


# Error handling test: mismatched lists should raise ValueError
try:
    give_bmi([1.8], [70, 80])
except ValueError:
    print("Mismatched lists test: passed")
else:
    print("Mismatched lists test: failed")
