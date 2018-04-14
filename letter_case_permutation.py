class Solution(object):
	def letterCasePermutation(self, S):
		res = ['']
		for ch in S:
			if ch.isalpha():
				res = [i+j for i in res for j in [ch.lower(), ch.upper()]]
			else:
				res = [i + ch for i in res]
		return res


	def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, '', res)
        return res 
    
    def dfs(self, S, path, res):
        if S=='':
            res.append(path)
            return 
        if S[0].isdigit():
            self.dfs(S[1:], path + S[0], res)
        else:
            self.dfs(S[1:], path + S[0].lower(), res)
            self.dfs(S[1:], path + S[0].upper(), res)