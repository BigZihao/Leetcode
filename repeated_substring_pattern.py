class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (s + s)[1:-1]
        return s in ss