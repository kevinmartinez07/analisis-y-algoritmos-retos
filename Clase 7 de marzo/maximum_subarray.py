class Solution:
    # dp[i] = max(nums[i], nums[i] + dp[i-1])
    # current guarda la mejor suma terminando en i.
    # best guarda la mejor suma global.
    # Tiempo: O(n)
    # Espacio: O(1)
    def maxSubArray(self, nums: list[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)

        return best