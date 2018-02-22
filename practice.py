class Solution():
	def combination(self, s):
		referdict = {'1':[],
		'2':['a','b','c'],
		'3':['d','e','f'],
		'4':['g','h','i'],
		'5':['j','k','l']
		'6':['m','n','o'],
		'7':['p','q','r','s'],
		'8':['t','u','v'],
		'9':['w','x','y','z']
		}
		res = []

		def dfs( digits, path, res):
			if s == '':
				res.append(path)
			k =  digits[0]
			for i in range(len(referdict[k])):
				path= path + referdict[k][i] + dfs( digits[1:], path, res)
			return res
		return res
		
		dfs(digits, '', res)
		return res


