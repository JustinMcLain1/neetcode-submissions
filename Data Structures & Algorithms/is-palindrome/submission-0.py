class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        word_list = list(s)
        word_list.reverse()
        if "".join(word_list) == s:
            return True
        return False