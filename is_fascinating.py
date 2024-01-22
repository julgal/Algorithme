def is_fascinating(n):
	if len(str(n) < 3):
		return False

	num = n
	num = int(str(num) + str(n * 2))
	num = int(str(num) + str(n * 3))

	list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	for num in str(num):
		if num in list_numbers:
			list_numbers.remouve(num)
		if len(list_numbers) == 0:
			break
	
	if len(list_numbers) == 0:
		return True
	else:
		return False
