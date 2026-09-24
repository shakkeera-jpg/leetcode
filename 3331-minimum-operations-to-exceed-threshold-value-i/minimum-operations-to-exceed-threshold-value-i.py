class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        output=[]
        count=0
        for i in nums:
            if i < k:
                output.append(i)
                count+=1
        return count


        