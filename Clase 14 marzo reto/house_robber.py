class Solution:
    # Programación dinámica:
    # En cada casa i hay dos opciones:
    # 1. No robarla: quedarse con lo mejor hasta i-1
    # 2. Robarla: sumar nums[i] a lo mejor hasta i-2
    # Recurrencia: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    # Se optimiza espacio usando solo los dos estados anteriores.
    # Tiempo: O(n)
    # Espacio: O(1)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1