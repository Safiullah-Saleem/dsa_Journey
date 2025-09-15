class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize pointers
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # calculate mid point correctly
            mid_point = (l + r) // 2
            
            # if target found
            if nums[mid_point] == target:
                return mid_point
            
            # check if left side is sorted
            if nums[l] <= nums[mid_point]:
                if nums[l] <= target < nums[mid_point]:
                    r = mid_point - 1
                else:
                    l = mid_point + 1
            else:
                # right side is sorted
                if nums[mid_point] < target <= nums[r]:
                    l = mid_point + 1
                else:
                    r = mid_point - 1
        
        return -1