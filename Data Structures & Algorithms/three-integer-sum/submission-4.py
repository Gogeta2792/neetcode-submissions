class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        start, left, right = 0, 0, len(nums) - 1

        res = []

        nums.sort()

        while start < len(nums) - 1:
            target = -nums[start]
            left = start + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    if [nums[start], nums[left], nums[right]] not in res:
                        res.append([nums[start], nums[left], nums[right]])
                    left += 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
            start += 1

        return res