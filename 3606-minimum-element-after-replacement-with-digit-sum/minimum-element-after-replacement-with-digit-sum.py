class Solution:
    def minElement(self, nums: List[int]) -> int:
        output=[]
        for i in nums:
            s=str(i)
            s2=0
            for i in s:
                s2+=int(i)
            output.append(s2)       
        return min(output)        

        

        