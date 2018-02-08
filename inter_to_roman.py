class Solution(object):
	def InterToRoman(self, num):
		values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
		list1 = ''
		for i in range(0, len(values)):
			while num >= values[i]:
				num- = values[i]
				list1 + = numerals[i]
		return list1
