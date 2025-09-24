def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
	elif type(object).__name__ == 'float' and object != object:
		print(f"Cheese: {object} {type(object)}")
	elif type(object).__name__ == 'int' and object == 0:
		print(f"Zero: {object} {type(object)}")
	elif type(object).__name__ == 'str' and object == "":
		print(f"Empty: {object} {type(object)}")
	elif type(object).__name__ == 'bool' and not object:
		print(f"Fake: {object} {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0