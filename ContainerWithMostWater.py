# Well, the key is to prove you will get the max every time you move the small node 

# the area is determined by the small one. say height=[1,2,3,4]. when you got the first area abs(4-1)*min(1,4)=3, this is determined by the left node 1
# you won't have anything bigger than 3 if you fix left node
# so this trick save you from looping another round, form O(n2) to O(n)

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
