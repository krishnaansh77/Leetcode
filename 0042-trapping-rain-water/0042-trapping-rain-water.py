class Solution(object):
    def trap(self, height):
        left=0
        right=len(height)-1

        leftmax=height[left] #can assign 0 too
        rightmax=height[right] #can assign 0 too
        water=0

        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                    
                else:
                    water=water+leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                
                else:
                    water=water+rightmax-height[right]
                right-=1

        return water

            
        
        