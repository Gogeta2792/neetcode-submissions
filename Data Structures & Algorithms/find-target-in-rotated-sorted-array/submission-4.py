class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        def helper(left, right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] > nums[mid]:
                if (nums[mid] <= target <= nums[right]):
                    return helper(mid, right)
                else:
                    return helper(left, mid)
                    
            if nums[left] < nums[mid]:
                if (nums[left] <= target <= nums[mid]):
                    return helper(left, mid)
                else:
                    return helper(mid, right)
            else: 
                return right if nums[right] == target else -1
        
        return helper(l, r)