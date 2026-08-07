class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1=[]
        for i in nums:
            nums1.append(i)
        return nums+nums1    