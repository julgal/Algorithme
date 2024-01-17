# Euler number
def factorial(nb):
	result = 1
	for num in range(1, nb+1):
		result *= num
	return result

def euler(n):
	euler_number = 0
	for i in range(n):
		euler_number += 1/factorial(i)
	return euler_number
