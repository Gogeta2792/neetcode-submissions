class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            target = -num

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]

                if curr == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif curr < target:
                    l += 1
                else:
                    r -= 1
        
        return res