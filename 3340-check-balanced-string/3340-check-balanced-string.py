class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
        for i in range(len(num)):  
            digit = int(num[i])  # Correctly access each digit
            if i % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit
        return even_sum == odd_sum  # Return statement is correctly indented