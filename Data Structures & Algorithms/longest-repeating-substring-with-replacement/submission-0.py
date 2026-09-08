class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        highest_freq = 0
        best=0
        for right,i in enumerate(s):
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            window_len = right - left +1
            highest_freq= max(highest_freq, freq[i])
            replacement = window_len - highest_freq
            while replacement>k:
                freq[s[left]] -=1
                left +=1
                window_len =right - left + 1
                replacement = window_len - highest_freq
                
            best = max(best, right - left + 1)
        return best

           
        
        

