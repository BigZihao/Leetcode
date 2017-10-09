
def myAtoi(self, str):
	str = str.strip()
	if str == "":
		return 0
	i = 0
	sign = 1 
	ret = 0
	length = len(str)
	MaxInt = (1 << 31) -1
	if str[i] == '+':
		i+=1
	elif str[i] == '-':
		i+=1
		sign=-1
	for i in range(i, length):
		if str[i] < '0' or str[i] > '9':
			break
		ret = ret * 10 + int(str[i])
		if ret > sys.maxint:
			break
	ret*= sign
	if ret >=MaxInt:
		return MaxInt
	if ret < MaxInt*-1:
		return MaxInt*-1-1
	return ret




def myAtoi(self, str):
	str = str.strip()
	str = re.findall('^[+\-]?\d+', str)

	try:
		result = int(''.join(str))
		MAX_INT = 2147483647
		MIN_INT = -2147483647
		if result > MAX_INT:
			return MAX_INT
		if result < MIN_INT:
			return MIN_INT
		return result
	except:
		return 0