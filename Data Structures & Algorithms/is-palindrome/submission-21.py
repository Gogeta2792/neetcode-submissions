class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(new) - 1
        while l <= r:
            if not new[l] == new[r]:
                return False
            l += 1
            r -= 1
        return True