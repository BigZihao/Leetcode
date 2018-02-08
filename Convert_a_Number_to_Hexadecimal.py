class Solution(object):
    def toHex(self, num):
        ret = ''
        letter = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if num == 0: return '0'
        if num < 0:
            num+=2**32
        while num:
            num, ret = num//16, ret + letter[num%16]
        return ret