class Solution:
    def removeInvalidParentheses(self, s: str):

        # Find minimum number of '(' and ')' to remove
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, left_remove, right_remove, balance, path):

            # End of string
            if index == len(s):

                if left_remove == 0 and right_remove == 0 and balance == 0:
                    result.add("".join(path))

                return

            ch = s[index]

            # Option 1: Remove current parenthesis
            if ch == '(' and left_remove > 0:
                dfs(
                    index + 1,
                    left_remove - 1,
                    right_remove,
                    balance,
                    path
                )

            elif ch == ')' and right_remove > 0:
                dfs(
                    index + 1,
                    left_remove,
                    right_remove - 1,
                    balance,
                    path
                )

            # Option 2: Keep current character
            if ch == '(':

                path.append(ch)

                dfs(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance + 1,
                    path
                )

                path.pop()

            elif ch == ')':

                # We cannot have more ')' than '('
                if balance > 0:

                    path.append(ch)

                    dfs(
                        index + 1,
                        left_remove,
                        right_remove,
                        balance - 1,
                        path
                    )

                    path.pop()

            else:
                # Letter
                path.append(ch)

                dfs(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance,
                    path
                )

                path.pop()

        dfs(
            0,
            left_remove,
            right_remove,
            0,
            []
        )

        return list(result)