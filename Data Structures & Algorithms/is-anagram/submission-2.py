class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if t==s:
            return True
        else:
            return False
        