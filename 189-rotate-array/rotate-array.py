class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums[len(nums)-k:len(nums)] = nums[len(nums)-k:len(nums)][::-1]
        nums[0:len(nums)-k]=nums[0:len(nums)-k][::-1]
        nums.reverse()
         

        