import sys

def check_args():
	#if len(sys.argv) != 2:
	try:
		value = sys.argv[2]
		print("AssertionEror: more than one argument is provided")
		return
	except IndexError:
		pass
	if type(sys.argv[1]).__name__ != 'int':
		print("AssertionError: argument is not an integer")
		return
	
check_args()