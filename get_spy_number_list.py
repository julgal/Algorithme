from math import prod

def spy_number(nb):
	sum_nb = sum(map(int, list(str(nb))))
	prod_nb = prod(map(int, list(str(nb))))
	return sum_nb == prod_nb

def get_spy_number_list(inf, sup):
	list_spy = []
	for i in range(inf, sup+1):
		if spy_number(i):
			list_spy.append(i)
	return list_spy
