def is_strobogrammatic(n):
	strobo = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

	if type(n) is int:
		n = str(n)

	left = 0
	right = len(n) - 1
	while right - left >= 0:
		if not n[left] in strobo.keys() or not n[right] in strobo.keys() or n[left] != strobo[n[right]]:
			return False
		right -= 1
		left += 1

	return True
