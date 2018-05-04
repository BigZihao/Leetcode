class Solution(object):
	def converToTitle(self, num):
		capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
		result = []
		while num>0:
			result.append(capitals[int((num-1)%26)])
			num = (num-1)//26
		result.reverse()
		return ''.join(result)

	def converToTitle2(self, num):
		num = int(num)
		alph = ''.join(map(chr, range(65, 91)))
		return (self.converToTitle((num-1)/len(alph)) if num>len(alph) else '') + alph[int((num-1)%len(alph))]

### Conversion from 10-ary numbers to 26-ary numbers. 
# The tricky part is the lack of the equivalent number '0' in the 26-ary system.
	def converToTitle4(self, num):
		res = ''
		while num:
			num, r = divmod(num - 1, 26)
			res = chr(r+ord('A')) + res
		return res

	def converToTitle5(self, num):
		res = ''
		base = ord('A')
		while num:
			num, r = divmod(num - 1, 26)
			res = '{}{}'.format(chr(base + r), res)
		return res


if __name__ == "__main__":
	print(Solution().converToTitle(66))
	print(Solution().converToTitle2(66))
	print(Solution().converToTitle4(66))
	print(Solution().converToTitle5(66))