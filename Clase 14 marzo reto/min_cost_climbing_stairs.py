class Solution:
    # Programación dinámica:
    # dp[i] representa el costo mínimo para llegar al escalón i.
    # Para llegar a i, se puede venir desde i-1 o desde i-2.
    # Recurrencia: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    # Se optimiza espacio usando solo los dos estados anteriores.
    # Tiempo: O(n)
    # Espacio: O(1)
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2 = 0  # dp[0]
        prev1 = 0  # dp[1]

        for i in range(2, len(cost) + 1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = current

        return prev1