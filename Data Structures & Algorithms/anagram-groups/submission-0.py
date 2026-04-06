class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we know there is 26 letters and we know the input

        res = defaultdict(list) #mapping charCount to list of Anagrams with hashmap

        #loop through string and form array of 26 zeros
        for s in strs:
            count = [0] * 26

            #to assign the index take ASCII value of current index
            #and subtract it from a to get the index value ASCII a - ASCII a = index 0
            # and ASCII z - ASCII a is going to give index 25 
            for c in s:
                count[ord(c) - ord("a")] += 1

            #group all anagrams with this count together
            #and we make it a tuple because lists are mutable and not hashable
            res[tuple(count)].append(s)
        
        return list(res.values())

        #this is O(m * n) where where m is number of strings given 
        # and n is the average length of each string
            