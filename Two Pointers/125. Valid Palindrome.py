class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for c in s:
            if not self.isValid(c):
                s = s.replace(c, "")
            
        for j in range(len(s)): 
            if s[j] != s[len(s)-1-j]:     
                return False
        return True
    
    def isValid(self, c: str):
        if (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")):
            return True
        return False
            
        