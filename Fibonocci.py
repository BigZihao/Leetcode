

## recursion
## O(2^n)
## 100 cannot be finished in time

def fibonicci(n):
	if n <=2:
		return 1
	else:
		return fibonicci(n-1)+fibonicci(n-2)

## exponential time 


## memorization

def fastFib(n, memo):
	global numCalls
	numCalls+=1
	print('fib1 called with',n)
	if not n in memo:
		memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
	return memo[n]

def fib1(n):
	memo = {0:1, 1:1}
	return fastFib(n, memo)

numCalls = 0
n = 100
res = fib1(n)
print('fib of', n, '=', res, 'numCall=', numCalls)


## memorization using decorator 
# 本质上，decorator就是一个返回函数的高阶函数
def memorize(f):
	cache = {}
	def decorated_function(*args):
		if args in cache:
			return cache[args]
		else:
			cache[args] = f(*args)
			return cache[args]
	return decorated_function

@memorize
def fib2(n):
	return 1 if n<=2 else fib2(n-2)+fib2(n-1)




## Bottom-up 
## O(n) time and O(1) space 
def fib3(n):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a+b
	return a

