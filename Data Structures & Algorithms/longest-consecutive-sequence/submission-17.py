class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                length = 0
                while num in seen:
                    length += 1
                    num +=1
                longest = max(longest, length)
        
        return longest