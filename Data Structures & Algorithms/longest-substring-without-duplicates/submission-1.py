class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        seen = {}
        left =0
        right = 0
        best =0
        current=0
        while right < len(s):
            if s[right] in seen and seen[s[right]]>=left:
                left = seen[s[right]] + 1
            
            current = right - left + 1
                
            seen[s[right]]=right
            right +=1
            best = max(best, current)
        return(best)