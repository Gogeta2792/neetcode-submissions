class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in hashmap:
                return [hashmap[c], i]
            else:
                hashmap[num] = i