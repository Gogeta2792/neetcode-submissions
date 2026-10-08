class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr_sum, curr_combination):
            if curr_sum == target:
                res.append(curr_combination)
                return
            elif curr_sum > target:
                return
            else:
                for i in range(idx, len(nums)):
                    backtrack(i, curr_sum + nums[i], curr_combination + [nums[i]])
        
        backtrack(0, 0, [])

        return res