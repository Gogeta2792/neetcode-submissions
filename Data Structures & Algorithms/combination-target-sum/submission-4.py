class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, currSum, combination):
            if currSum == target:
                res.append(combination)
                return
            elif currSum > target:
                return
            else:
                for i in range(idx, len(nums)):
                    helper(i, currSum + nums[i], combination + [nums[i]])
        
        helper(0, 0, [])

        return res