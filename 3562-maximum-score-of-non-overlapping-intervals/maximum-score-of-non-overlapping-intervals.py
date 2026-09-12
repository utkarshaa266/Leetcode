from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # start, end, weight, original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by starting point
        arr.sort()

        starts = [x[0] for x in arr]

        # next interval whose start > current end
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best (score, indices)
        # from i onward, choosing at most k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # 1. Skip current interval
                skip = dp[i + 1][k]

                # 2. Take current interval
                next_score, next_indices = dp[nxt[i]][k - 1]

                take = (
                    arr[i][2] + next_score,
                    tuple(sorted((arr[i][3],) + next_indices))
                )

                # Choose maximum score
                if take[0] > skip[0]:
                    dp[i][k] = take

                # Same score -> lexicographically smaller
                elif take[0] == skip[0]:
                    dp[i][k] = min(take, skip)

                else:
                    dp[i][k] = skip

        return list(dp[0][4][1])