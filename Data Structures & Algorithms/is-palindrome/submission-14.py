class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [c.lower() for c in s if c.isalnum()]

        left, right = 0, len(new) - 1

        while left <= right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        
        return True