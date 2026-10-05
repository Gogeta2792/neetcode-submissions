class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for start, num in enumerate(nums):
            if start > 0 and num == nums[start-1]:
                continue

            left, right = start + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < -num:
                    left += 1
                elif curr_sum > -num:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res