class Solution:
    def fib(self, n: int) -> int:
        # first we will define the base case 
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # now the recurseve case 
        return self.fib(n-2)+self.fib(n-1)