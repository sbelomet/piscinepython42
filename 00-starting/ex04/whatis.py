import sys

def is_it_odd_or_even(number: int) -> None:
	my_list = ['Even', 'Odd']
	print(f"I'm {my_list[number % 2]}")

def check_args() -> None:
	#if len(sys.argv) < 2:
	try:
		value = sys.argv[2]
		print("AssertionEror: more than one argument is provided")
		return
	except IndexError:
		pass

	try:
		number = int(sys.argv[1])
		is_it_odd_or_even(number)
	except IndexError:
		pass
	except ValueError:
		print(f"AssertionError: argument is not an integer")
		return

check_args()