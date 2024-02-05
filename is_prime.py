def is_prime(nb):
	if nb < 2:
		return False
	for d in range(2, nb):
		if nb % d == 0:
			return False
	return True

if __name__ == "__main__":
    try:
        number = int(input("Enter a number:"))
        if is_prime(number):
            print(f"The number {number} is prime.")
        else:
            print(f"The number {number} is not prime.")
    except:
        print("Error, you don't have enter a number.")
