class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Initialize max sum as the smallest number
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)  # Extend or start new subarray
            max_sum = max(max_sum, current_sum)  # Update max sum

        return max_sum