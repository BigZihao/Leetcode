#Pascal's Triangle

## 算法时间复杂度应该是O(1+2+3+...+n)=O(n^2)，


def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows==0:
        return []
    result = [[1]]
    for i in range(1, numRows):
        use = result[i-1] + [0]
        result.append([use[k-1]+use[k] for k in range(len(use))])
    return result
        


def generate2(self, numRows):
	res = [[1]]
	for i in range(1, numRows):
		res+=[map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1])]
	return res[:numRows]