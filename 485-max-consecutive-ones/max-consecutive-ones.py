class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxcount=0

        for i in nums:
            if i==1:
                count+=1
                if count>maxcount:
                    maxcount=count
            else :
                count=0
        return maxcount