class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        result1=abs(x-z)
        result2=abs(y-z)
        if result1<result2:
            return 1
        elif result1==result2:
            return 0
        else:
            return 2   
        