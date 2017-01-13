# Well, the key is to prove you will the result every time you move the small node 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        res=0
        while left<right:
            water=min(height[left],height[right])*abs(left-right)
            res=max(res,water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res
