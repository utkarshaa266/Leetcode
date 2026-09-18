class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # Find first and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Try to create a valid substring starting from each character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character appeared before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                # Expand to include all occurrences of this character
                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((left, right))

        # Greedy: choose interval with smallest ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for left, right in intervals:
            if left > end:
                ans.append(s[left:right + 1])
                end = right

        return ans