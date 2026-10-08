class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            target = -num
            l, r = idx + 1, len(nums) - 1
            
            while l < r:
                curr_sum = nums[l] + nums[r]

                if curr_sum == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                elif curr_sum < target:
                    l += 1
                
                else:
                    r -= 1

        return res            