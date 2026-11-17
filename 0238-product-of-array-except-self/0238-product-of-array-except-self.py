class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        prefix = 1

        # Left to Right
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Right to Left
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
        
        
        