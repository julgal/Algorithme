def is_trimorphic(n):
	len_n = len(str(n))

	if str(n**3)[-len_n:] == str(n):
		return True

	return False
