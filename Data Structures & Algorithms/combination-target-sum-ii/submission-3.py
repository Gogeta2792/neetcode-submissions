class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted([c for c in candidates if c <= target])
        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            else:
                curr.append(nums[i])
                backtrack(i + 1, curr, total + nums[i])
                curr.pop()

                while (i + 1) < len(nums) and nums[i + 1] == nums[i]:
                    i += 1
                
                backtrack(i + 1, curr, total)

                return
        
        backtrack(0, [], 0)

        return res