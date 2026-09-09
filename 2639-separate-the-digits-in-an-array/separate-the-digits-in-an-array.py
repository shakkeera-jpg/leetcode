class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s1=""
        output=[]
        for i in nums:
            s1+=str(i)
        for i in s1:
            output.append(int(i))
        return output     
  