#To test the function, remove the hashtag in front of each print

#Creation of a function tenth_power
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

#Creation of a function to find the first three multiples
def first_three_multiples(num):
	print(num*1)
	print (num*2)
	print (num*3)
	return (num*3) 

#print(first_three_multiples(10))

#Creation of a function to calculate the tip with two arguments "total" and "percentage"
def tip(total, percentage):
	return total * (percentage / 100)

#print(tip(10,25))

#Creation of a repetitive function
def introduction(first_name, last_name):
	print(last_name, ", ", first_name, last_name)

#print(introduction("James", "Bond"))

#Creation of a calculator
def dog_years(name, age):
	dog_age = age * 7
	print(name, ", you are ", dog_age, " years old in dog years")

#print(dog_years("Lola",27))

#Create a four parameters functions for calculation
def lots_of_maths(a, b, c, d):
	print(a+b)
	print(c-d)
	print((a+b) * (c-d))
	return ((a+b) * (c-d)) % a

#print(lots_of_maths(1, 2, 3, 4))





















