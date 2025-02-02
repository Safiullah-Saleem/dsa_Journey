class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0  # Start with 0 as the initial max wealth
        
        for account in accounts:  # Loop through each customer's accounts
            wealth = sum(account)  # Sum up the money in all accounts for this customer
            max_wealth = max(max_wealth, wealth)  # Update the max wealth if current wealth is higher
        
        return max_wealth  # Return the maximum wealth
