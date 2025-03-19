class Solution:
    def isPalindrome(self, s: str) -> bool:
         # Step 1: Convert to lowercase
        s = s.lower()

        # Step 2: Initialize two pointers
        left, right = 0, len(s) - 1

        # Step 3: Loop until pointers meet
        while left < right:

            # Ignore non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare letters from both ends
            if s[left] != s[right]:
                return False        #not a Palindrome
         
            # Move pointers inward
            left += 1
            right -= 1

        return True
        






