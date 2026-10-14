class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen:
                length = 1
                target = num + 1
                while target in seen:
                    length += 1
                    target += 1
                longest = max(longest, length)
        
        return longest