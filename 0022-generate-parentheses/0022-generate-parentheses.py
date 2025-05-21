class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O(C**N ∗ N)
# Space: O(C**N ∗ N)
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # we choose either of the options below
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res