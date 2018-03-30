class Solutions(object):
	def LetterCombinations(self, digits):

		## time complexity O(4^n)
		def dfs(num, string, res):
			if num == length:
				res.append(string)
				return
			for letter in dict[digits[num]]:
				dfs(num+1, string+letter, res)

		### string is the current path along the graph using DFS, once you hit the num, then store the string to res

		dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        length = len(digits)
        if length == 0:
        	return res
        dfs(0, '', res)
        return res


    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]


##这种组合类的问题，如果求出所有的组合方案，一定是指数级别的。

##3^n - 4^n 是对的，因为你有n位电话号码，每一位的时候，可能按出来的字母是3-4个，所以就是 (3~4)^n