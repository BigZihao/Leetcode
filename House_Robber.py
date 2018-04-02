

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now


    def rob2(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[-1]
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i] +max(nums[:i-1]))
        return max(nums[-1],nums[-2])

# Based on the recursive formula:

# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )


if __name__ == "__main__":
    assert Solution().rob([1,2,4,5,3,3,3,1,34,62,9])