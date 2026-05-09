class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        a = 1
        b = 2

        if n <= 1:
            return 1

        for i in range(3, n + 1):
            current = a + b
            a = b
            b = current
        return b
