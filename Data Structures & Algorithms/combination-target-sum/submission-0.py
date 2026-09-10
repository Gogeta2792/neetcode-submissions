class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(curr, start, combination):
            if curr == 0:
                res.append(combination)
            if curr < 0:
                return None
            if curr > 0:
                for i, num in enumerate(nums[start:]):
                    helper(curr - num, i + start, combination + [num])
        
        helper(target, 0, [])
        
        return res