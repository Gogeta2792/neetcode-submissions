class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            
            else:
                for i in range(idx, len(nums)):
                    curr.append(nums[i])
                    backtrack(i, curr, total + nums[i])
                    curr.pop()
        
        backtrack(0, [], 0)

        return res