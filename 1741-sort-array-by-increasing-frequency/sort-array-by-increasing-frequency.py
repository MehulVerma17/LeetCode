class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        '''
        d1=dict(Counter(nums))
        d1=sorted(d1.items(),key=lambda x:x[1] )
        print(d1)
        l=[]
        for i,j in d1:
            for _ in range(j):
                l.append(i)
        return l
        '''
        return sorted(sorted(nums,reverse=1),key=nums.count)