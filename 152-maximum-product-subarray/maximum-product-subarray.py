class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxnum=nums[0]
        minnum=nums[0]
        m=nums[0]
        temp=0

        for i in range(1,len(nums)):
            if nums[i] >0:
                maxnum=max(nums[i],maxnum*nums[i])
                minnum=min(nums[i],minnum*nums[i])
            elif nums[i]==0:
                maxnum=0
                minnum=0
            else:
                temp=maxnum
                maxnum=max(nums[i],minnum*nums[i])
                minnum=min(nums[i],temp*nums[i])
            m=max(m,maxnum)
        return m
