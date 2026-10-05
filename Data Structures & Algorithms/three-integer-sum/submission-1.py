class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()

        for i, num in enumerate(nums):
            seen = {}
            target = -num
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    tmp = tuple(sorted((nums[i], nums[j], seen[complement])))
                    triplets.add(tmp)
                else:
                    seen[nums[j]] = nums[j]
        
        res = []

        for t in triplets:
            res.append(list(t))
        
        return res