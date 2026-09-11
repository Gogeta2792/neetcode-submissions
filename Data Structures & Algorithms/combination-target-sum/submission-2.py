class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(curr_sum, idx, combination):
            if curr_sum == target:
                res.append(combination)
                return
            if curr_sum > target:
                return
            else:
                idx_add = 0
                for num in nums[idx:]:
                    helper(curr_sum + num, idx + idx_add, combination + [num])
                    idx_add += 1
        
        helper(0, 0, [])

        return res