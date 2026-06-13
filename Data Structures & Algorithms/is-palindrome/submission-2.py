class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            while left<right and not ((s[left] >= 'A' and s[left] <='Z') or (s[left] >= 'a' and s[left] <='z') or (s[left] >= '0' and s[left] <='9')):
                left += 1
            while left<right and not ((s[right] >= 'A' and s[right] <='Z') or (s[right] >= 'a' and s[right] <='z') or (s[right] >= '0' and s[right] <='9')):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
