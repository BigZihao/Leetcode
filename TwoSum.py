## O(n), only loop the list once



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i in range(len(nums)):
            x=nums[i]
            if target-x in dict:
                return (dict[target-x],i)
            dict[x]=i
