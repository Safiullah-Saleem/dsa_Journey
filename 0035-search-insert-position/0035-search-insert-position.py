class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:  # Use '<=' for binary search
            mid = (l + r) // 2

            if nums[mid] == target:  # Compare value, not index
                return mid
            elif nums[mid] < target:
                l = mid + 1  # Move right
            else:
                r = mid - 1  # Move left
    
        return l  # Return 'l'