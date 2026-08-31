class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numbers = set(nums)

        for num in nums:
            if num - 1 not in numbers:
                count, length = 1, 1
                while num + count in numbers:
                    count += 1
                    length +=1
                longest = max(longest, length)
        
        return longest