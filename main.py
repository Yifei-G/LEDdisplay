from numToLed import numToLed

while True:

	try:
		inputNum = input("Please enter non-negative numbers:")
		assert inputNum.isdigit()
		numToLed(inputNum)
	except AssertionError:
		print("You have entered an invalid input, please enter only non-negative numbers!")