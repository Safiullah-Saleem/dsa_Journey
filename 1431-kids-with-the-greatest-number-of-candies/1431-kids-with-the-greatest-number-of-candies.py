class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       # Step 1: Find the maximum number of candies
        max_candies = max(candies)
    
        # Step 2: Initialize the result list
        result = []
    
        # Step 3: Iterate over the candies list and check the condition
        for i in range(len(candies)):
            # After adding extraCandies, check if it's >= max_candies
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        # Step 4: Return the result after processing all kids
        return result