class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(s, open, close):
            # Complete valid string
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add opening bracket
            if open < n:
                backtrack(s + "(", open + 1, close)

            # Add closing bracket
            if close < open:
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)

        return result