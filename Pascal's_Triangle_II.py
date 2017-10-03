##Pascal's Triangle II

def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res=[1]
    for i in range(1, rowIndex+1):
        res = list(map(lambda x, y: x+y, [0]+res, res+[0]))
    return res
    