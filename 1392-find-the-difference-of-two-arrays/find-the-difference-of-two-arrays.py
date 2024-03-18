class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set=set(nums1)
        nums2set=set(nums2)

        res1,res2=set(),set()

        for i in nums1:
            if i not in nums2set:
                res1.add(i)

        for i in nums2:
            if i not in nums1set:
                res2.add(i)
        
        return [res1,res2]