# Spy number 123: 1*2*3 == 1+2+3
from math import prod

def spy_number(nb):
	sum_nb = sum(map(int, list(str(nb))))
	result_nb = prod(map(int, list(str(nb))))
	return sum_nb == result_nb
