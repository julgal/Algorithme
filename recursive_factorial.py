def recursive_factorial(nb):
	if nb == 0 or nb == 1:
		return 1
	return nb * recursive_factorial(nb-1)
