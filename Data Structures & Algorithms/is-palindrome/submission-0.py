class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pulita = [c.lower() for c in s if c.isalnum()]
        
        return pulita == pulita[::-1]
        