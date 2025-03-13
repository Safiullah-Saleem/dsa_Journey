class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # Dictionary to store last seen index of each number
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True  # Found a duplicate within range k
            seen[num] = i  # Store the latest index of this number
        
        return False  # No nearby duplicates found
