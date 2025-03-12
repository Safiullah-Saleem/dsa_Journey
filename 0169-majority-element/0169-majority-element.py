class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        return nums[len(nums) // 2]  # Return the middle element