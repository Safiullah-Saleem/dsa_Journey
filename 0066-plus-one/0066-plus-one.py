class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):  # Loop from last to first digit
            if digits[i] < 9:
                digits[i] += 1  # Add 1 to the current digit
                return digits  # Return the updated list
            
            digits[i] = 0  # If the digit is 9, change it to 0
        
        return [1] + digits  # If all digits were 9, add 1 at the beginning