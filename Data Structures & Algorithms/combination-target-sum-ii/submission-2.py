class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted([c for c in candidates if c <= target])
        res = []

        def backtrack(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or idx >= len(nums):
                return
            
            else:
                curr.append(nums[idx])
                backtrack(idx + 1, curr, total + nums[idx])
                curr.pop()

                while (idx + 1) < len(nums) and nums[idx + 1] == nums[idx]:
                    idx += 1
                
                backtrack(idx + 1, curr, total)
        
        backtrack(0, [], 0)

        return res