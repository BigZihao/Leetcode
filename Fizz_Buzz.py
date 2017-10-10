## Fizz Buzz

def fizzBuzz(self, n):
	return ['Fizz'* (not i % 3) + 'Buzz'*(not i % 5) or str(i) for i in range(1, n+1)]



def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    result=[]
    for i in range(1, n+1):
        if i % 5==0 and i % 3 ==0:
            result.append(str("FizzBuzz"))
        elif i % 5 == 0:
            result.append(str("Buzz"))
        elif i % 3 == 0:
            result.append(str("Fizz"))
        else:
            result.append(str(i))
    return result