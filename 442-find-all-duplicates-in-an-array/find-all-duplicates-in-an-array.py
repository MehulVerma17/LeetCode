class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        l=[]
        nums.sort()

        while left<len(nums) and right<len(nums):
            if nums[left]==nums[right]:
                l.append(nums[left])
            left+=1
            right+=1
        return l