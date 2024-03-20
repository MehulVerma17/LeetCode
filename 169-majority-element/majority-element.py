class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
       
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
        
        
        '''
        count_dict=Counter(nums)
        key=list(count_dict.keys())
        val=list(count_dict.values())
        maxc=max(count_dict.values())

        maxn=val.index(maxc)
        return key[maxn]
        '''
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
        
