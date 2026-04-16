class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counts = 0
        for n in nums:
            if counts == 0:
                candidate = n
            
            counts += 1 if candidate == n else -1

        return candidate
        