class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
                
            target = -num
            l, r = idx + 1, len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]

                if curr == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                
                elif curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
        
        return res