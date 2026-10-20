class Solution(object):
    def maxArea(self, height):
        max=0
        left=0
        right=len(height)-1
        while left<right:
            
            width=abs(left-right)
            h=min(height[left],height[right])
            area=width*h
            if area>max:
                max=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max

        