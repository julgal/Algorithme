def get_dividers(nb):
	dividers_list = []
	for divider in range(1, nb+1):
		if nb % divider == 0:
			dividers_list.append(divider)
	return dividers_list

print(get_dividers(20))
