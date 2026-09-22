class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # Each node:
        # [product % k, count of prefixes for each remainder]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(A, B):
            prodA, cntA = A
            prodB, cntB = B

            # Product of combined segment
            prod = (prodA * prodB) % k

            cnt = [0] * k

            # Prefixes completely inside A
            for r in range(k):
                cnt[r] += cntA[r]

            # Prefixes that contain all of A
            # and continue into B
            for r in range(k):
                new_r = (prodA * r) % k
                cnt[new_r] += cntB[r]

            return [prod, cnt]

        def build(node, left, right):
            if left == right:
                remainder = nums[left] % k

                tree[node][0] = remainder
                tree[node][1][remainder] = 1
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, pos, value):
            if left == right:
                remainder = value % k

                tree[node] = [remainder, [0] * k]
                tree[node][1][remainder] = 1

                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, right, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, left, right, ql, qr):

            # Completely inside range
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            # Query only left side
            if qr <= mid:
                return query(
                    node * 2,
                    left,
                    mid,
                    ql,
                    qr
                )

            # Query only right side
            if ql > mid:
                return query(
                    node * 2 + 1,
                    mid + 1,
                    right,
                    ql,
                    qr
                )

            # Query both sides
            A = query(
                node * 2,
                left,
                mid,
                ql,
                qr
            )

            B = query(
                node * 2 + 1,
                mid + 1,
                right,
                ql,
                qr
            )

            return merge(A, B)

        # Build tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            nums[index] = value

            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Get information for nums[start ... n-1]
            result = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            # result[1] = prefix counts
            answer.append(result[1][x])

        return answer