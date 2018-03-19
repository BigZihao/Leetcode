# Steve has a string, , consisting of  lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after operation.

# Steve wants to reduce  as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

# Note: If the final string is empty, print Empty String .


def super_reduce(strings):
	res = [] # stack
	for c in strings:
		if res and res[len(res)-1]==c:
			res.pop()
		else:
			res.append(c)
	res = ''.join(res)
	return res or 'Empty'

s = input().strip()
result = super_reduced_string(s)
print(result)

