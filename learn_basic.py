
def f(x):
	return x*x

r = map(f, [1,2,3,4,5,6,7])
list(r)

from functools import reduce
def fn(x, y):
	return x*10 + y

reduce(fn, [1, 3, 5, 7, 9])

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

reduce(fn, map(char2num, '13579'))

def str2int(s):
	return reduce(lambda x, y: 10*x + y, map(char2num, s))

