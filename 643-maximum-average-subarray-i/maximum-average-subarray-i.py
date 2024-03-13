class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=0
        for i in range(k):
            sum1+=nums[i]

        maxsum=sum1

        startindex=0
        endindex=k

        while endindex<len(nums):
            sum1-=nums[startindex]
            startindex+=1

            sum1+=nums[endindex]
            endindex+=1

            maxsum=max(maxsum,sum1)

        return maxsum/k