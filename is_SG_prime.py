# Prime number of Sophie Germain
def is_prime(nb):
	if nb < 2:
		return False
	for d in range(2, nb):
		if nb % d == 0:
			return False
	return True

def is_SG_prime(nb):
	if is_prime(nb) and is_prime(nb*2+1):
		return True
	else:
		return False
