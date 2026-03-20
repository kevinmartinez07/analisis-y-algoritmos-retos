class Solution:
    # Programación dinámica:
    # dp[i] representa las formas de llegar al escalón i.
    # Recurrencia: dp[i] = dp[i-1] + dp[i-2]
    # Casos base: dp[1] = 1, dp[2] = 2
    # Se optimiza espacio usando solo los dos estados anteriores.
    # Tiempo: O(n)
    # Espacio: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1