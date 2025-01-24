class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()  # Go back to the parent directory
            elif log == "./":
                continue  # Stay in the current directory
            else:
                stack.append(log)  # Move into the specified directory
        
        return len(stack)  # The size of the stack represents the depth