class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # fist solution 
        # N = len(nums)
        # for i in range(N):
        #     nums.append(nums[i])
        # return nums

        # second solution 
        # return nums * 2

        # third solution 
    #    return nums + nums
        result = []
        for num in nums:
            result.append(num)
    # After this loop: result = [1, 2, 1]
        for num in nums:
            result.append(num)
    # After this loop: result = [1, 2, 1, 1, 2, 1]
        return result





        
        
        # first output is [1,2,1]
    
            # second output is [1,2,1,1,2,1]
        
