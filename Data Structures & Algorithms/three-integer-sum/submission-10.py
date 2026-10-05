class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for start, num in enumerate(nums):
            if start > 0 and num == nums[start-1]:
                continue
            target = -num
            left = start + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return res