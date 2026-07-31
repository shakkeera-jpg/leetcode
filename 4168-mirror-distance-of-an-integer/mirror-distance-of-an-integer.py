class Solution:
    def mirrorDistance(self, n: int) -> int:
        n1=str(n)
        res=""
        output=0
        for i in n1:
            res= i + res
        output=abs(n-int(res))
        return output    


        