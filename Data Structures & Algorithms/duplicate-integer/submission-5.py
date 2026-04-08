class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False

        #a hashset can also be used for this and it would be cleaner
        #since you wouldnt need a key-value pair like the hashmap above