class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen=[]
        result=[]
        for i in nums:
            if i in seen:
                result.append(i)
            else:
                seen.append(i)
        return result            