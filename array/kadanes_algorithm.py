# Kadane's algorithm
# For finding a max sum subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Keep track of global max subarray
        mx = nums[0]

        # Keep track of current subarray sum
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            # Take max of either extending current running sum or starting new
            maxEnding = max(maxEnding + nums[i], nums[i])

            # Record global max
            mx = max(mx, maxEnding)

        return mx
