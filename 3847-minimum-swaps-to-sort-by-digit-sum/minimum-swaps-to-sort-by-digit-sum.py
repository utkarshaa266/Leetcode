class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        index = {num: i for i, num in enumerate(nums)}

        swaps = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i] or index[sorted_nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index[sorted_nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps