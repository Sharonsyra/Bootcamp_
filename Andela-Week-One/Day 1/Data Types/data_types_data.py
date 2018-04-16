def data_type(num):
	if type(num) is str:
		return len(num)
	elif num is None:
		return "no value"
	elif type(num) is bool:
		return num
	elif type(num) is int:
		if num < 100:
			return "less than 100"
		elif num ==100:
			return "equal to 100"
		return "more than 100"
	elif type(num) is list:
		if len(num) < 3:
			return None
		else:
			return num[2]
		
