class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # If it's an opening bracket, push to stack
            if char in "([{":
                stack.append(char)
            
            # If it's a closing bracket
            else:
                if not stack:   # stack empty → no opening bracket
                    return False

                top = stack.pop()

                # Manually check each case
                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False

        # At the end stack must be empty
        return not stack


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []  # this will store opening brackets
#         mapping = {')': '(', ']': '[', '}': '{'}  
#         # mapping tells which opening bracket matches each closing one

#         for char in s:
#             if char in mapping:  
#                 # if char is a closing bracket (like ), ], or })

#                 # Pop the top element from stack if not empty
#                 # If stack is empty, we use '#' as a dummy value
#                 top = stack.pop() if stack else '#'

#                 # Check if the popped element matches the correct opening bracket
#                 if mapping[char] != top:
#                     return False  # mismatch found → not valid
#             else:
#                 # If it's an opening bracket ( (, {, [ ), push onto stack
#                 stack.append(char)

#         # At the end, stack should be empty if all brackets matched
#         return not stack
