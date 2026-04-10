class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm = {}

        for num in nums:
            hashm[num] = hashm.get(num,0) + 1
        
            sorted_items = sorted(hashm.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result        