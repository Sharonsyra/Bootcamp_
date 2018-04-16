def find_missing(firstarray, secondarray):
	if firstarray == secondarray:
		return 0
	elif firstarray != secondarray:
		a = set(firstarray)
		b = set(secondarray)
		c = a ^ b
		return list(c)[0]
