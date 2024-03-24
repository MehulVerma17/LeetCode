class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        left=0
        right=1
        
        nums.sort()

        while left<len(nums) and right<len(nums):
            if nums[left]==nums[right]:
                return nums[left]
            left+=1
            right+=1
            

