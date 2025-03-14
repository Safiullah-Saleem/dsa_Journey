class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Step 1: Define search range

        while left <= right:  # Step 2: Continue while search range is valid
            mid = (left + right) // 2  # Step 3: Find middle index

            if nums[mid] == target:  # Step 4: If mid element is target, return index
                return mid
            elif nums[mid] < target:  # Step 5: If mid element is smaller, search right
                left = mid + 1
            else:  # Step 6: If mid element is larger, search left
                right = mid - 1

        return -1  # Step 7: If target not found, return -1