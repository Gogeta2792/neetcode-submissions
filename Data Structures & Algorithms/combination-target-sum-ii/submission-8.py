class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums = sorted([c for c in candidates if c <= target])
        if not nums:
            return res
        
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i > len(nums) - 1:
                return
            else:
                curr.append(nums[i])
                backtrack(i + 1, curr, total + nums[i])
                curr.pop()

                while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                backtrack(i + 1, curr, total)

                return
        
        backtrack(0, [], 0)

        return res