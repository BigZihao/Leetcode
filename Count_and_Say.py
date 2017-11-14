

# re.sub(pattern, repl, string, count)

def countAndSay(self, n):
	s = '1'
	for _ in range(n - 1):
		s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
	return s



def countAndSay(self, n):
	s = '1'
	for _ in range(n-1):
		s = ''.join(str(len(list(group)))) + digit for digit, group in itertools.groupby(s)
	return s


def count(self, n):
	t = ''; count = 0; curr = '#'
	for i in s:
		if i!=curr:
			if curr!='#':
				t+=str(count) + curr
			curr=i
			count = 1
		else:
			count+=1
	t+=str(count)+curr
	return t

def countAndSay(self, n):
	s = '1'
	for i in range(2, n+1):
		s = self.count(s)
	return s



def countAndSay(self, n):
	s = ['1']
	result = '1'
	for i in range(n-1):
		start = 0
		temp = []
		while start < len(s):
			count = 1
			next = start + 1
			while next < len(s) and s[start] == s[next]:
				next+=1
				count+=1
			temp.append(str(count))
			temp.append(s[start])
			start = next
		result = ''.join(temp)
		s=temp
	return result