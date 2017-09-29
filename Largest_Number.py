

## define a new comparison to sort the list

def largestNumber(self, nums):
    nums = sorted(nums, cmp=lambda x, y: 1 if int(str(x) + str(y)) < int(str(y) + str(x)) else -1)
    largest = ''.join(map(str, nums))
    if largest[0]=='0':
        return '0'
    return largest
    

