class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 1000
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == target:
                    return threesum
                
                if abs(threesum - target) < abs(result - target):
                    result = threesum
                
                if threesum < target:
                    left += 1
                elif threesum > target:
                    right -= 1
            
        return result