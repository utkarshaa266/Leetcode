class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        # dp[x] stores the count of subarrays ending at the current index 
        # whose product modulo k is x.
        dp = [0] * k
        
        for num in nums:
            rem = num % k
            next_dp = [0] * k
            
            # Transition from the previous subarrays ending at the prior index
            for x in range(k):
                if dp[x] > 0:
                    next_dp[(x * rem) % k] += dp[x]
            
            # Start a new subarray consisting of only the current element
            next_dp[rem] += 1
            
            # Add the counts of all subarrays ending at the current index to the total answer
            for x in range(k):
                ans[x] += next_dp[x]
                
            dp = next_dp
            
        return ans
