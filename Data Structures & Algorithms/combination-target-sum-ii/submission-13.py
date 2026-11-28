class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted([c for c in candidates if c <= target])
        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(nums) or total > target:
                return
            
            else:
                curr.append(nums[i])
                backtrack(i + 1, curr, total + nums[i])
                curr.pop()

                j = i + 1

                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                
                backtrack(j, curr, total)

                return
        
        backtrack(0, [], 0)

        return res