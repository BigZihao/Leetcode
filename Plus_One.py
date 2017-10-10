##Pl us_One



#recursion

def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits = digits or [0]
    if digits[-1] == 9:
        digits = self.plusOne(digits[:-1]) + [0]
    else:
        digits[-1]+=1
    return digits


## like cheat

def plusOne(self, digits):
	return [int(x) for x in str(int(''.join([str(x) for x in digits]))+1)]


## reverse loop over all digits

def plusOne(self, digits):
	for i in range(len(digits)-1, -1, -1):
		digits[i] = digits[i] + 1 if digits[i]<9 else 0
		if digits[i]:
			return digits
	digits.insert(0, 1)
	return digits
