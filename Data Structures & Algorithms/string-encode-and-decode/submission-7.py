class Solution:

    def encode(self, strs: List[str]) -> str:
        new_list = []
        for i in range(len(strs)):
            count = len(strs[i])
            new_list.append(str(count))
            new_list.append(strs[i])
        return "#".join(new_list)

    def decode(self, s: str) -> List[str]:
        i=0
        final_list = []
        if len(s)==0:
            return final_list
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            count = int(s[i:j])
            start = j+1
            end = start + count
            final_list.append(s[start:end])
            i = end + 1

        return(final_list)

