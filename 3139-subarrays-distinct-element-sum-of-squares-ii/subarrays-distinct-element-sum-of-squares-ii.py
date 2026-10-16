
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right, val):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                tree[node] = (tree[node] + val * val * (end - start + 1)
                              + 2 * val * 0) % MOD
                lazy[node] += val
                return

            mid = (start + end) // 2
            update(node * 2, start, mid, left, right, val)
            update(node * 2 + 1, mid + 1, end, left, right, val)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        def add(node, start, end, left, right, val):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                length = end - start + 1
                tree[node] = (tree[node] + 2 * val * lazy[node] * length
                              + val * val * length) % MOD
                lazy[node] += val
                return

            mid = (start + end) // 2
            add(node * 2, start, mid, left, right, val)
            add(node * 2 + 1, mid + 1, end, left, right, val)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        # Correct lazy propagation implementation
        sum_tree = [0] * (4 * n)
        square_tree = [0] * (4 * n)
        lazy_add = [0] * (4 * n)

        def apply(node, length, val):
            square_tree[node] = (
                square_tree[node] + 2 * val * sum_tree[node]
                + val * val * length
            ) % MOD
            sum_tree[node] = (sum_tree[node] + val * length) % MOD
            lazy_add[node] = (lazy_add[node] + val) % MOD

        def push(node, start, end):
            if lazy_add[node] == 0 or start == end:
                return
            mid = (start + end) // 2
            apply(node * 2, mid - start + 1, lazy_add[node])
            apply(node * 2 + 1, end - mid, lazy_add[node])
            lazy_add[node] = 0

        def range_add(node, start, end, left, right, val):
            if left <= start and end <= right:
                apply(node, end - start + 1, val)
                return

            push(node, start, end)
            mid = (start + end) // 2

            if left <= mid:
                range_add(node * 2, start, mid, left, right, val)
            if right > mid:
                range_add(node * 2 + 1, mid + 1, end, left, right, val)

            sum_tree[node] = (
                sum_tree[node * 2] + sum_tree[node * 2 + 1]
            ) % MOD
            square_tree[node] = (
                square_tree[node * 2] + square_tree[node * 2 + 1]
            ) % MOD

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            # Every subarray ending at i that contains a new
            # occurrence of x gets its distinct count increased by 1.
            range_add(1, 0, n - 1, left, i, 1)

            ans = (ans + square_tree[1]) % MOD
            last[x] = i

        return ans
