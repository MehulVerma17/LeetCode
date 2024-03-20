class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
        '''
        maxc=0
        maxn=0
        for i in nums:
            c=nums.count(i)
            if c>maxc:
                maxc=c
                maxn=i
        return maxn
        '''
        
