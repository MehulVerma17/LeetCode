class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        a=dict(Counter(nums))
        l=[]
        for i in a:
            if a[i] > n/3:
                l.append(i)

        return l