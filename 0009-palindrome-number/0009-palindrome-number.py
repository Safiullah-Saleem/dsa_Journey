class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]  # Convert to string and compare with its reverse