class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h_set = set(nums)
        return len(h_set) != len(nums) 