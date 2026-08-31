class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_consecutive = 0

        for num in nums:
            count = 0
            length = 0
            if num - 1 not in seen:
                while num + count in seen:
                    count += 1
                    length += 1
                longest_consecutive = max(longest_consecutive, length)
        
        return longest_consecutive