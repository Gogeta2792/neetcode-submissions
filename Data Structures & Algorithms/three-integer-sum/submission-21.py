class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while i < len(nums):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return res