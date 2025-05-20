class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # to handle the duplicate
            # go over the duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) -1

            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    # to get the triplets                    
                    res.append([nums[left], nums[right], nums[i]])
                    
                    # to handle duplicates
                    # take the pointer further till the last duplicate
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                    # to skip the last duplicate or to get to the new elements     
                    left += 1
                    right -= 1

                elif s>0:
                    right -= 1
                else:
                    left += 1
        return res
    
        