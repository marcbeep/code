class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fib(n):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b

            return b
        
        return fib(n)
