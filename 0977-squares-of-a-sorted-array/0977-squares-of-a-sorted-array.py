class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         # Square each element
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2  # Corrected from sqrt() to squaring
        
        # Sort the squared numbers
        nums = sorted(nums)  # Moved sorting outside the loop
        
        return nums