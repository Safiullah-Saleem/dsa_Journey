class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check if it's out of order
                count += 1
        return count <= 1  # A valid rotated array has at most one break