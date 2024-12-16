import sys

arg_len = len(sys.argv)

try:
	if arg_len == 1:
		print()
	elif arg_len != 2:
		raise AssertionError("AssertionError: more than one argument is provided")
	else:
		arg = sys.argv[1]
		try:
			arg = int(arg)
		except:
			raise AssertionError("AssertionError: argument is not an integer")
		if (arg % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
except AssertionError as msg:
	print(msg)