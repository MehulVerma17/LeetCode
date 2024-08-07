class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        max_len = 0

        for i in n:
            if i - 1 not in n:
                curr_num=i
                curr_length=1

                while curr_num + 1 in n:
                    curr_num +=1
                    curr_length +=1
                
                max_len = max(max_len, curr_length)
        return max_len