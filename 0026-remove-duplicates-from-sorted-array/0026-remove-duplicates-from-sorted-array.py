class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 
        for r in range(1, len (nums)): 
            if nums[r] != nums[r - 1]: 
                nums[l] = nums[r]  
                l += 1 
        return l
        # if not nums:
        #     return 0
        # j = 0
        # for i in range(1, len(nums)):
        #      if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums[i]
        # return j + 1


