
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)

        n = len(squares)
        return sum(squares[n // 2:]) - sum(squares[:n // 2])
