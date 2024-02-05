def factorial(nb):
	if nb == 0 or nb == 1:
		return 1

	result = 1
	for num in range(1, nb+1):
		result *= num
	return result

if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(factorial(number))
    except:
        print("Error. You not have enter a number.")
