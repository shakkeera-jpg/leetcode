class Solution:
    def maxDistinct(self, s: str) -> int:
        sub=[]
        output=0
        for i in s:
            if i not in sub:
                output+=1
                sub.append(i)
        return output         

        