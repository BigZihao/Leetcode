## ZigZag Conversion

def convert(self, s, numRows):
	if numRows == 1 or numRows>=len(s):
		return s
	L = [''] * numRows
	index, step = 0, 1
	for x in s:
		L[index]+=x
		if index == 0:
			step = 1
		elif index == numRows-1:
			step = -1
		index+ = step
	return ''.join(L)



def convert(self, s, numRows):
	if numRows == 1: return s
	rows = ['']*numRows
	num = (numRows - 1)*2
	for i, item in enumerate(s):
		if i % num >= numRows:
			rows[(num - i % num) % numRows]+=item
		else:
			rows[i % num]+=item
	return ''.join(rows)