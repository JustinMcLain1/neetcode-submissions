class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 1:
                count +=1
                if res < count:
                    res = count
            else:
                count = 0
        return res