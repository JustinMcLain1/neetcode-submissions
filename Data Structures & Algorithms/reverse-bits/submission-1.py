class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        for i in range(32):
            bit = (n >> i) & 1
            count += (bit << (31 - i))
        return count
