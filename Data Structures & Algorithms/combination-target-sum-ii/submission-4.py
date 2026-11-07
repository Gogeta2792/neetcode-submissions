class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted([c for c in candidates if c <= target])
        res = []

        def backtrack(idx, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if idx > len(nums) - 1 or total > target:
                return
            
            else:
                curr.append(nums[idx])
                backtrack(idx + 1, total + nums[idx], curr)
                curr.pop()

                while (idx + 1) < len(nums) and nums[idx] == nums[idx + 1]:
                    idx += 1
                
                backtrack(idx + 1, total, curr)

                return
        
        backtrack(0,0,[])

        return res