#To test the function, remove the hashtage in front of each print

#Creation of a fucntion tenth_power
def tenth_power(num):
	return num**10

#print(tenth_power(2))

#Creation of a square root function
def square_root(num):
	return num**0.5

#print(square_root(100))

#Creation of a win percentage function with two paramteters (win, lose)
def win_percentage(win,lose):
	return win / (win + lose) * 100

#print(win_percentage(5,5))

#Creation of an average function
def average(num1, num2):
	return (num1 + num2) / 2

#print(average(1,100))

#Creation of a remainder function
def remainder(num1, num2):
	return (num1 * 2) % (num2 / 2)

#print(remainder(15,14))