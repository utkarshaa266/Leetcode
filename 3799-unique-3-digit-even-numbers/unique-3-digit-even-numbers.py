class Solution:
    def totalNumbers(self, digits):
        nums = set()

        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue

                    # First digit cannot be 0
                    if digits[i] == 0:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(num)

        return len(nums)