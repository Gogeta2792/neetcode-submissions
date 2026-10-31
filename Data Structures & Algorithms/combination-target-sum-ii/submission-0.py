class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted([c for c in candidates if c <= target])
        res = []

        if not nums:
            return res

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr)
                return
            
            elif total > target or i == len(nums):
                return

            else:
                backtrack(i + 1, curr + [nums[i]], total + nums[i])

                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                backtrack(i + 1, curr, total)

        backtrack(0, [], 0)

        return res            