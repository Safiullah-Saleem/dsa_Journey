class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
     result = []
    # Iterate through each element in nums
     for i in range(len(nums)):
        count = 0
        # Compare with all other elements to find how many are smaller
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        # Add the count to the result list
        result.append(count)
     return result