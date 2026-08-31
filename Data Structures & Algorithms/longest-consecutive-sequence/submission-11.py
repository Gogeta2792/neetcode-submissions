class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            count = 1
            if num - 1 not in seen:
                while num + count in seen:
                    count += 1 
                longest = max(longest, count)
        
        return longest