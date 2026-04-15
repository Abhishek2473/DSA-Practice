class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for c in s.lower():
            if c.isalnum():
                new+=c
        return new==new[::-1]
        