## We just keep track of the index of the added elements, so when we remove them, we copy the last one into it.

## From Python docs (https://wiki.python.org/moin/TimeComplexity) 
## we know that list.append() takes O(1), both average and amortized. 
## Dictionary get and set functions take O(1) average, so we are OK.

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.position = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.position:
            self.nums.append(val)
            self.position[val] = len(self.nums)-1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.position:
            idx, last = self.position[val], self.nums[-1]
            self.nums[idx] = last
            self.position[last] = idx
            self.nums.pop()
            self.position.pop(val)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums)-1)]
        

